from django.urls import path

from .views import (Dashboard, LoginPage, SponsorListAPIView, SponsorCreateAPIView, SponsorUpdateAPIView, SponsorRetrieveAPIView,
                    StudentListAPIView, StudentCreateAPIView, StudentUpdateAPIView, StudentRetrieveAPIView,
                    SponsorToStudentCreateAPIView, SponsorToStudentUpdateAPIView, SponsorToStudentDestroyAPIView)


urlpatterns = [
    path('', Dashboard.as_view(), name='dashboard'),
    path('login/', LoginPage.as_view(), name='login'),
    path('sponsor/', SponsorListAPIView.as_view(), name='sponsor_list'),
    path('sponsor/<int:pk>/', SponsorRetrieveAPIView.as_view(), name='sponsor_detail'),
    path('sponsor/create/', SponsorCreateAPIView.as_view(), name='sponsor_create'),
    path('sponsor/update/<int:pk>', SponsorUpdateAPIView.as_view(), name='sponsor_update'),
    path('student/', StudentListAPIView.as_view(), name='student_list'),
    path('student/<int:pk>/', StudentRetrieveAPIView.as_view(), name='student_detail'),
    path('student/create/', StudentCreateAPIView.as_view(), name='student_create'),
    path('student/update/<int:pk>', StudentUpdateAPIView.as_view(), name='student_update'),
    path('sponsor-student/create/', SponsorToStudentCreateAPIView.as_view(), name='sponsor_student_create'),
    path('sponsor-student/update/<int:pk>', SponsorToStudentUpdateAPIView.as_view(), name='sponsor_student_update'),
    path('sponsor-student/delete/<int:pk>', SponsorToStudentDestroyAPIView.as_view(), name='sponsor_student_delete'),
]
