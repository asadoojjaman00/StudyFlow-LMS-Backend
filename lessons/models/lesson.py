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

   
    lesson_type = models.CharField(
        choices=LessonType.choices,
        null=True,
        blank=True
    )
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=1000, blank=True, null=True)
    lesson_link = models.URLField(null=True, blank=True)
    start_date = models.DateTimeField(null=True,blank=True)
    end_date = models.DateTimeField(null=True,blank=True)

    is_active = models.BooleanField(default=True)
    

    def __str__(self):
        return self.title