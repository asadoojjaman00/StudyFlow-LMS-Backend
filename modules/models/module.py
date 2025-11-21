from courses.models.course import Course
from django.db import models

class Module(models.Model):
    course   = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name='modules'
    )

    title = models.CharField(max_length=250,)
    description = models.TextField(blank=True)
    order  = models.PositiveIntegerField(default=0)



    total_live_class_count = models.CharField(max_length=2,null=True,blank=True)
    total_assignment_count = models.CharField(max_length=2, null=True, blank=True)
    total_test_count  = models.CharField(max_length=2, null=True, blank=True)
    

    start_day = models.DateTimeField(null=True, blank=True)
    end_day = models.DateTimeField(null= True, blank = True)
    
    is_active = models.BooleanField(default=False)
    is_unlocked = models.BooleanField(default=False)

    def __str__(self):
        return self.course.title