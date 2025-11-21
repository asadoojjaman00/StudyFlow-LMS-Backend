from django.db import models
from modules.models.module import Module


class Lesson(models.Model):
    class LessonType(models.TextChoices):
        LIVE = 'live', 'Live'
        RECODED = 'recorded', 'Recorded'
        ASSIGNMENT = 'assignment' , 'Assignment'
        TEST = 'test', 'Test'
        
    module = models.ForeignKey(
        Module,
        on_delete=models.CASCADE,
        related_name='lessons'
    )

    title = models.CharField(max_length=255)
    lesson_type = models.CharField(
        choices=LessonType.choices,
        null=True,
        blank=True
    )