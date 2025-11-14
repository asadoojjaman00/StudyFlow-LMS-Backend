# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from users.models.User_model import User
# from users.models.UserProfiles_models import StudentProfile,InstructorProfile





# @receiver(post_save, sender = User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         if instance.role == 'student':
#             StudentProfile.objects.get_or_create(user= instance)
#         elif instance.role == 'instructor':
#             InstructorProfile.objects.get_or_create(user=instance)
#     else:
#         try:
#             old_user = User.objects.get(pk=instance.pk)
#         except User.DoesNotExist:
#             return
#         if old_user.role != instance.role:
#             StudentProfile.objects.filter(user= instance).delete()
#             InstructorProfile.objects.filter(user=instance).delete()

#             if instance.role == 'student':
#                 StudentProfile.objects.get_or_create(user=instance)
#             elif instance.role == 'Instructor':
#                 InstructorProfile.objects.get_or_create(user=instance)