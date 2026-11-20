from django.urls import path

from . import views

urlpatterns = [
    path('departments/', views.create_department),
    path('job-positions/', views.create_job_position),
    path('candidates/', views.create_candidate),
    path('resumes/', views.upload_resume),
    path('screening-results/<int:pk>/', views.get_screening_result),
    path('interview-question-sets/<int:pk>/', views.get_interview_question_set),
]