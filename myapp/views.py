from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateAPIView, RetrieveAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework import status

from .models import Sponsor, Student, SponsorToStudent
from .serializers import SponsorSerializer, StudentSerializer, SponsorCreateSerializer, StudentCreateSerializer, SponsorToStudentSerializer


class SponsorListAPIView(ListAPIView):
    queryset = Sponsor.objects.all()
    serializer_class = SponsorSerializer

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

    filter_backends = (DjangoFilterBackend, SearchFilter)
    filterset_fields = ['student_type', 'otm']
    search_fields = ['full_name']


class StudentRetrieveAPIView(RetrieveAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentCreateAPIView(CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentCreateSerializer


class StudentUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentCreateSerializer
    

  
class SponsorToStudentCreateAPIView(CreateAPIView):
    queryset = SponsorToStudent.objects.all()
    serializer_class = SponsorToStudentSerializer

