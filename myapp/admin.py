from django.contrib import admin

from .models import SponsorToStudent, Sponsor, Student, OTM


@admin.register(Sponsor)
class SponsorAdmin(admin.ModelAdmin):
    list_display = ['id', 'type', 'full_name', 'sponsor_summa', 'spend_summa']

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'student_type', 'full_name', 'allocated_summa', 'kontrakt_summa']

@admin.register(SponsorToStudent)
class SponsorToStudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'sponsor', 'student', 'summa']


admin.site.register(OTM)
