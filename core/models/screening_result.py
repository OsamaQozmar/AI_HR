from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from .candidate import Candidate
from .job_position import JobPosition


class ScreeningResult(models.Model):
    RECOMMENDATION_CHOICES = [
        ('proceed', 'Proceed'),
        ('hold', 'Hold'),
        ('reject', 'Reject'),
    ]

    candidate = models.ForeignKey(
        Candidate, on_delete=models.CASCADE, related_name='screening_results'
    )
    job_position = models.ForeignKey(
        JobPosition, on_delete=models.CASCADE, related_name='screening_results'
    )
    score = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(100)]
    )
    strengths = models.JSONField(default=list, blank=True)
    missing_skills = models.JSONField(default=list, blank=True)
    recommendation = models.CharField(max_length=10, choices=RECOMMENDATION_CHOICES)
    summary = models.TextField(blank=True)
    raw_report = models.JSONField(default=dict, blank=True)
    generated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'screening_results'
        ordering = ['-generated_at']

    def __str__(self):
        return f'{self.candidate.full_name} - {self.job_position.title} ({self.score})'