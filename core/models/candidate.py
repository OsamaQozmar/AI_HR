from django.db import models


class Candidate(models.Model):
    full_name = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=30, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'candidates'
        ordering = ['-created_at']

    def __str__(self):
        return self.full_name