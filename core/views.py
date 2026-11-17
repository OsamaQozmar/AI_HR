from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import InterviewQuestionSet, ScreeningResult
from .serializers import (
    CandidateSerializer,
    DepartmentSerializer,
    InterviewQuestionSetSerializer,
    JobPositionSerializer,
    ResumeSerializer,
    ScreeningResultSerializer,
)


class CreateView(APIView):
    serializer_class = None

    def post(self, request):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DepartmentCreateView(CreateView):
    serializer_class = DepartmentSerializer


class JobPositionCreateView(CreateView):
    serializer_class = JobPositionSerializer


class CandidateCreateView(CreateView):
    serializer_class = CandidateSerializer


class ResumeUploadView(CreateView):
    serializer_class = ResumeSerializer


class ScreeningResultDetailView(APIView):
    def get(self, request, pk):
        result = get_object_or_404(ScreeningResult, pk=pk)
        return Response(ScreeningResultSerializer(result).data)


class InterviewQuestionSetDetailView(APIView):
    def get(self, request, pk):
        question_set = get_object_or_404(InterviewQuestionSet, pk=pk)
        return Response(InterviewQuestionSetSerializer(question_set).data)