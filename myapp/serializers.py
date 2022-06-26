from rest_framework import serializers
from myapp.models import Sponsor, Student, SponsorToStudent, OTM


class SponsorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sponsor
        fields = '__all__'


class SponsorCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sponsor
        fields = [
            'type',
            'full_name',
            'phone_number',
            'sponsor_summa',
            'company'
        ]


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'


class StudentCreateSerializer(serializers.ModelSerializer):
    otm = serializers.PrimaryKeyRelatedField(queryset=OTM.objects.all())
    
    class Meta:
        model = Student
        fields = [
            'full_name',
            'phone_number',
            'otm',
            'student_type',
            'kontrakt_summa'
        ]


class SponsorToStudentSerializer(serializers.ModelSerializer):
    sponsor = serializers.PrimaryKeyRelatedField(queryset=Sponsor.objects.all())
    # student = serializers.PrimaryKeyRelatedField(queryset=Student.objects.all())


    class Meta:
        model = SponsorToStudent
        fields = ['sponsor', 'student', 'summa']

    def validate(self, attrs):
        student_id = attrs.get('student')
        sponsor_id = attrs.get('sponsor')
        summa = attrs.get('summa')

        if sponsor_id.sponsor_summa < summa:
            raise serializers.ValidationError('pul yetarli emas')

        if student_id.summa_mod < summa:
            raise serializers.ValidationError(f'{student_id.full_name} ga {student_id.summa_mod} shuncha pul yetarli. siz esa {summa} shuncha kirityapsiz')

        
        sponsor_id.spend_summa += summa
        sponsor_id.sponsor_summa -= summa
        sponsor_id.save()

        student_id.allocated_summa += summa
        student_id.save()

        return attrs
    
    def create(self, validated_data):
        student_id = validated_data.get('student')
        sponsor_id = validated_data.get('sponsor')
        summa = validated_data.get('summa')
        ss = SponsorToStudent.objects.filter(student=student_id, sponsor=sponsor_id).first()
        print(ss)
        if ss is not None:
            ss.summa += summa
            ss.save()
            return validated_data
        return super().create(validated_data)
    
