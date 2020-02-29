from django.db import models
from django.utils import timezone


class Question(models.Model):
    type = models.CharField(max_length=30)  # have to be a unique value
    question = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    sample_answer = models.TextField(null=True, blank=True)
    difficulty = models.IntegerField(null=True, blank=True)
    frequency = models.IntegerField(null=True, blank=True)
    pub_date = models.DateField(timezone.now())

    def __str__(self):
        return self.type
