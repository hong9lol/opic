from django.db import models

# Create your models here.


class Question(models.Model):
    type = models.CharField(max_length=30)
    question = models.TextField()
    description = models.TextField()
    sample_answer = models.TextField()
    difficulty = models.IntegerField()
    frequency = models.IntegerField()

    def __str__(self):
        return self.question
