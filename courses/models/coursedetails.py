from django.db import models
from .course import Course
from users.models.User_model import User


class CourseDetails(models.Model):
    course = models.OneToOneField(
        Course,
        on_delete=models.CASCADE,
        related_name="course_details"
    )
    demo_class_video = models.URLField(null=True, blank=True)
    price          = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    discount_price = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True )
    total_live_classes = models.CharField(max_length=5, null=True,blank=True)
    total_projects  = models.CharField(max_length=5, null=True,blank=True)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)