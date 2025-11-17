from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver
from courses.models import Enrollment,Course,CourseDetails


@receiver(post_save, sender=Enrollment)
def increase_course_enroll_count(sender, instance, created, **kwargs):
    if created:
        course = instance.course
        course.total_enrolled = course.enrollments.count()
        course.save()

@receiver(post_delete, sender = Enrollment)
def decrease_course_enroll_count(sender, instance, **kwargs):
    course = instance.course
    course.total_enrolled = course.enrollments.count()
    course.save()

@receiver(post_save, sender = Course)
def create_course_details(sender, instance, created, **kwargs):
    if created:
        CourseDetails.objects.get_or_create(course=instance)