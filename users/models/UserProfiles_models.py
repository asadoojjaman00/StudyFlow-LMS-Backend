from django.db import models
from .Base_user_profile import BaseUserProfile


"""

Student profile model extend by base-user-profile

"""
class StudentProfile(BaseUserProfile):

    class SkillChoice(models.TextChoices):
        web_development   = 'web development', 'Web Development'
        app_development   = 'app development', 'App Development'
        digital_marketing = 'business & marketing', 'Business & Marketing'
        ai_engineer       = 'ai engineering', 'AI Engineering'
        data_engineering  = 'data engineering', 'Data Engineering'
        cyber_security    = 'cyber security', 'Cyber Security'
        graphic_design    = 'graphic design', 'Graphic Design'
         

    class Education(models.TextChoices):
        msc     = 'msc', 'MSC'
        bsc     = 'bsc', 'BSC'
        diploma = 'diploma', 'Diploma'
        hsc     = 'hsc', 'HSC'
        ssc     = 'ssc',  'SSC'
        mba     = 'mba', 'MBA'
        bba     = 'bba', 'BBA'
        other   = 'other', 'Other'
        
    career_focus = models.CharField(
        max_length=100,
        choices=SkillChoice.choices,
        blank=True,
        null=True
    )
    education = models.CharField(
        max_length=20,
        choices=Education.choices,
        blank=True,
        null=True
    )
    
    def __str__(self):
        return self.user.username

"""

Instructor profile model extend by base-user-profile


"""

class InstructorProfile(BaseUserProfile):
    
    experience_year    = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.user.username


