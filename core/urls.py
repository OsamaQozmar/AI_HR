from django.urls import path

from .views import (
    CandidateCreateView,
    DepartmentCreateView,
    InterviewQuestionSetDetailView,
    JobPositionCreateView,
    ResumeUploadView,
    ScreeningResultDetailView,
)

urlpatterns = [
    path('departments/', DepartmentCreateView.as_view()),
    path('job-positions/', JobPositionCreateView.as_view()),
    path('candidates/', CandidateCreateView.as_view()),
    path('resumes/', ResumeUploadView.as_view()),
    path('screening-results/<int:pk>/', ScreeningResultDetailView.as_view()),
    path('interview-question-sets/<int:pk>/', InterviewQuestionSetDetailView.as_view()),
]