from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import InterviewQuestionSet, ScreeningResult
from .serializers import (
    CandidateSerializer,
    DepartmentSerializer,
    InterviewQuestionSetSerializer,
    JobPositionSerializer,
    ResumeSerializer,
    ScreeningResultSerializer,
)


def create_object(serializer_class, request):
    serializer = serializer_class(data=request.data, context={'request': request})
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def create_department(request):
    return create_object(DepartmentSerializer, request)


@api_view(['POST'])
def create_job_position(request):
    return create_object(JobPositionSerializer, request)


@api_view(['POST'])
def create_candidate(request):
    return create_object(CandidateSerializer, request)


@api_view(['POST'])
def upload_resume(request):
    return create_object(ResumeSerializer, request)


@api_view(['GET'])
def get_screening_result(request, pk):
    result = get_object_or_404(ScreeningResult, pk=pk)
    serializer = ScreeningResultSerializer(result, context={'request': request})
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_interview_question_set(request, pk):
    question_set = get_object_or_404(InterviewQuestionSet, pk=pk)
    serializer = InterviewQuestionSetSerializer(question_set, context={'request': request})
    return Response(serializer.data, status=status.HTTP_200_OK)