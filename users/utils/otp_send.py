from celery import shared_task
from django.core.mail import send_mail
from django.contrib.auth import get_user_model

User = get_user_model()

@shared_task
def send_otp_email_task(user_id, otp):
    user = User.objects.get(id=user_id)
    subject =  f"HI {user.full_name}!"
    message = f"Your OTP is: {otp}\n don't share anyone"
    send_mail(subject, message, from_email=None, recipient_list=[user.email])

    
