from django.db import models
from django.utils import timezone


class Question(models.Model):
    type = models.CharField(max_length=60, null=True)
    title = models.CharField(max_length=60, null=True)
    question = models.TextField(max_length=500, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    sample_answer = models.TextField(null=True, blank=True)
    difficulty = models.IntegerField(null=True, blank=True)
    frequency = models.IntegerField(null=True, blank=True)
    pub_date = models.DateField(timezone.now())

    def __str__(self):
        return self.type
