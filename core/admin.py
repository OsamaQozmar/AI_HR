from django.contrib import admin

from .models import (
    Candidate,
    Department,
    InterviewQuestionSet,
    JobPosition,
    Resume,
    ScreeningResult,
)


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    search_fields = ('name',)


@admin.register(JobPosition)
class JobPositionAdmin(admin.ModelAdmin):
    list_display = ('title', 'department', 'created_at')
    list_filter = ('department',)
    search_fields = ('title',)


@admin.register(Candidate)
class CandidateAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'phone', 'created_at')
    search_fields = ('full_name', 'email')


@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display = ('candidate', 'file', 'uploaded_at')
    search_fields = ('candidate__full_name',)


@admin.register(ScreeningResult)
class ScreeningResultAdmin(admin.ModelAdmin):
    list_display = ('candidate', 'job_position', 'score', 'recommendation', 'generated_at')
    list_filter = ('recommendation', 'job_position', 'generated_at')
    search_fields = ('candidate__full_name', 'candidate__email')

@admin.register(InterviewQuestionSet)
class InterviewQuestionSetAdmin(admin.ModelAdmin):
    list_display = ('candidate', 'job_position', 'generated_at')
    list_filter = ('job_position',)
    search_fields = ('candidate__full_name',)