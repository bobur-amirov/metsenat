from django.db import models
from django.db.models import Sum


class Sponsor(models.Model):
    class Type(models.TextChoices):
        YURIDIK = 'yuridik'
        JISMONIY = 'jismoniy'

    class Status(models.TextChoices):
        NEW = 'new'
        MODERATION = 'moderation'
        CONFIRMED = 'confirmed'
        REJECTED = 'relected'

    type = models.CharField(max_length=20, choices=Type.choices, default=Type.JISMONIY)
    full_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=13, unique=True)
    sponsor_summa = models.DecimalField(max_digits=20, decimal_places=2, default=0)
    company = models.CharField(max_length=255, null=True, blank=True)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    status = models.CharField(max_length=10, choices=Status.choices, default=Status.NEW)

    @property
    def spend_summa(self):
        result = SponsorToStudent.objects.filter(sponsor__id = self.id).aggregate(summa = Sum('summa'))['summa']
        return result

    @property
    def summa_mod(self):
        if self.spend_summa:
            return self.sponsor_summa - self.spend_summa
        return self.sponsor_summa

    def __str__(self) -> str:
        return self.full_name


class OTM(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Student(models.Model):
    class Type(models.TextChoices):
        BACHELOR = 'bachelor'
        MASTER = 'master'

    full_name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=13, unique=True)
    student_type = models.CharField(max_length=8, choices=Type.choices, default=Type.BACHELOR)
    otm = models.ForeignKey(OTM, on_delete=models.CASCADE)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    kontrakt_summa = models.DecimalField(max_digits=20, decimal_places=2, default=0)

    @property
    def allocated_summa(self):
        result = SponsorToStudent.objects.filter(student__id = self.id).aggregate(summa = Sum('summa'))['summa']
        return result
    
    @property
    def summa_mod(self):
        if self.allocated_summa:
            return self.kontrakt_summa - self.allocated_summa
        return self.kontrakt_summa

    def __str__(self) -> str:
        return self.full_name


class SponsorToStudent(models.Model):
    sponsor = models.ForeignKey(Sponsor, on_delete=models.SET_NULL, null=True)
    student = models.ForeignKey(Student, on_delete=models.SET_NULL, null=True)
    summa = models.DecimalField(max_digits=20, decimal_places=2, default=0)

    # def __str__(self) -> str:
    #     return f'{self.sponsor.full_name} to {self.student.full_name} sponsor' 


