from django.utils import timezone
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from django.contrib.auth import authenticate
from rest_framework.parsers import JSONParser
from rest_framework.authtoken.models import Token
from django.db.models import Sum
from rest_framework.pagination import LimitOffsetPagination

from .models import Sponsor, Student, SponsorToStudent
from .serializers import SponsorSerializer, StudentSerializer, SponsorCreateSerializer, StudentCreateSerializer, SponsorToStudentSerializer


class LoginPage(APIView):
    def post(self, request):
        parser_classes = JSONParser
        username = request.data['username']
        password = request.data['password']
        if username is None or password is None:
            return Response({'mess': "Login yoki Parol kiritmadingiz!"})
        user = authenticate(username=username, password=password)
        if not user:
            return Response({'mess': "Login yoki Parol xato!"})
        token, create = Token.objects.get_or_create(user=user)
        return Response({'token': str(token), 'mess': "Xush kelibsiz!"})


class Dashboard(APIView):
    def get(self, request):
        date = timezone.now()
        year = date.year
        sponsor_all = {}
        student_all = {}

        sponsor_total = Sponsor.objects.aggregate(total = Sum('sponsor_summa'))
        student_total = Student.objects.aggregate(total = Sum('kontrakt_summa'))

        for i in range(1, 13):
            sponsor_all[i] = Sponsor.objects.filter(created__year=year, created__month=i).count()
            student_all[i] = Student.objects.filter(created__year=year, created__month=i).count()
        
        
        context = {
            'sponsor_all':sponsor_all,
            'student_all':student_all,
            'sponsor_total': sponsor_total,
            'student_total':student_total,
        }
        return Response(context)


class SponsorListAPIView(ListAPIView):
    queryset = Sponsor.objects.all()
    serializer_class = SponsorSerializer
    pagination_class = LimitOffsetPagination

    filter_backends = (DjangoFilterBackend, SearchFilter)
    filterset_fields = {
        'status': ['exact'],
        'sponsor_summa': ['exact'],
        'created': ['gte', 'lte'],
    }
    search_fields = ['full_name']


class SponsorRetrieveAPIView(RetrieveAPIView):
    queryset = Sponsor.objects.all()
    serializer_class = SponsorSerializer

class SponsorCreateAPIView(CreateAPIView):
    queryset = Sponsor.objects.all()
    serializer_class = SponsorCreateSerializer


class SponsorUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Sponsor.objects.all()
    serializer_class = SponsorCreateSerializer


class StudentListAPIView(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    pagination_class = LimitOffsetPagination

    filter_backends = (DjangoFilterBackend, SearchFilter)
    filterset_fields = ['student_type', 'otm']
    search_fields = ['full_name']


class StudentRetrieveAPIView(APIView):

    def get(self, request, *args, **kwargs):
        id = kwargs.get('pk')
        student = Student.objects.get(id=id)
        student_serializer = StudentSerializer(student)
        ss = SponsorToStudent.objects.filter(student = student)
        ss_serializer = SponsorToStudentSerializer(ss, many=True)

        context = {
            'student':student_serializer.data,
            'student_sponsor': ss_serializer.data
        }
        return Response(context)

class StudentCreateAPIView(CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentCreateSerializer


class StudentUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentCreateSerializer
    

  
class SponsorToStudentCreateAPIView(CreateAPIView):
    queryset = SponsorToStudent.objects.all()
    serializer_class = SponsorToStudentSerializer


class SponsorToStudentUpdateAPIView(UpdateAPIView):
    queryset = SponsorToStudent.objects.all()
    serializer_class = SponsorToStudentSerializer


class SponsorToStudentDestroyAPIView(DestroyAPIView):
    queryset = SponsorToStudent.objects.all()
    serializer_class = SponsorToStudentSerializer