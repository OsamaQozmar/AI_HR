from django.db import models

from .candidate import Candidate
from .job_position import JobPosition
from .screening_result import ScreeningResult


class InterviewQuestionSet(models.Model):
    candidate = models.ForeignKey(
        Candidate, on_delete=models.CASCADE, related_name='question_sets'
    )
    job_position = models.ForeignKey(
        JobPosition, on_delete=models.PROTECT, related_name='question_sets'
    )
    screening_result = models.ForeignKey(
        ScreeningResult, on_delete=models.CASCADE, related_name='question_sets'
    )
    technical_questions = models.JSONField(default=list, blank=True)
    behavioral_questions = models.JSONField(default=list, blank=True)
    follow_up_questions = models.JSONField(default=list, blank=True)
    generated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'interview_question_sets'
        ordering = ['-generated_at']

    def __str__(self):
        return f'Questions for {self.candidate.full_name} - {self.job_position.title}'