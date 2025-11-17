from django.db import models
from .course import Course
from users.models.User_model import User


class Enrollment(models.Model):
    student = models.ForeignKey(
        User,
        limit_choices_to={'role':'student'},
        on_delete=models.CASCADE,
        related_name='enrollments'
    )

    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name='enrollments'
    )

    enroll_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('student', 'course')
        