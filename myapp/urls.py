from django.urls import path

from .views import (SponsorListAPIView, SponsorCreateAPIView, SponsorUpdateAPIView, SponsorRetrieveAPIView,
                    StudentListAPIView, StudentCreateAPIView, StudentUpdateAPIView, StudentRetrieveAPIView,
                    SponsorToStudentCreateAPIView)


urlpatterns = [
    path('sponsor/', SponsorListAPIView.as_view(), name='sponsor_list'),
    path('sponsor/<int:pk>/', SponsorRetrieveAPIView.as_view(), name='sponsor_detail'),
    path('sponsor/create/', SponsorCreateAPIView.as_view(), name='sponsor_create'),
    path('sponsor/update/<int:pk>', SponsorUpdateAPIView.as_view(), name='sponsor_update'),
    path('student/', StudentListAPIView.as_view(), name='student_list'),
    path('student/<int:pk>/', StudentRetrieveAPIView.as_view(), name='student_detail'),
    path('student/create/', StudentCreateAPIView.as_view(), name='student_create'),
    path('student/update/<int:pk>', StudentUpdateAPIView.as_view(), name='student_update'),
    path('sponsor-student/', SponsorToStudentCreateAPIView.as_view(), name='sponsor_student_create'),
]
