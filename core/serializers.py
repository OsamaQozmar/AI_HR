import os

from rest_framework import serializers

from .models import (
    Candidate,
    Department,
    InterviewQuestionSet,
    JobPosition,
    Resume,
    ScreeningResult,
)

ALLOWED_RESUME_EXTENSIONS = ['.pdf', '.docx', '.txt']


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ['id', 'name', 'description', 'created_at']
        read_only_fields = ['id', 'created_at']


class JobPositionSerializer(serializers.ModelSerializer):
    department_name = serializers.CharField(source='department.name', read_only=True)

    class Meta:
        model = JobPosition
        fields = [
            'id',
            'department',
            'department_name',
            'title',
            'description',
            'required_skills',
            'created_at',
        ]
        read_only_fields = ['id', 'created_at']


class CandidateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidate
        fields = ['id', 'full_name', 'email', 'phone', 'created_at']
        read_only_fields = ['id', 'created_at']


class ResumeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resume
        fields = ['id', 'candidate', 'file', 'uploaded_at']
        read_only_fields = ['id', 'uploaded_at']

    def validate_file(self, value):
        extension = os.path.splitext(value.name)[1].lower()
        if extension not in ALLOWED_RESUME_EXTENSIONS:
            raise serializers.ValidationError(
                'Only PDF, DOCX and TXT files are accepted.'
            )
        return value


class ScreeningResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScreeningResult
        fields = [
            'id',
            'candidate',
            'job_position',
            'score',
            'strengths',
            'missing_skills',
            'recommendation',
            'summary',
            'raw_report',
            'generated_at',
        ]
        read_only_fields = fields


class InterviewQuestionSetSerializer(serializers.ModelSerializer):
    class Meta:
        model = InterviewQuestionSet
        fields = [
            'id',
            'candidate',
            'job_position',
            'screening_result',
            'technical_questions',
            'behavioral_questions',
            'follow_up_questions',
            'generated_at',
        ]
        read_only_fields = fields