from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import get_user_model
from users.utils.otp_send import send_otp_email_task
from users.utils.otpgenerate import (
    can_resend,
    generate_otp,
    set_otp_in_redis,
    set_resend_block
)
User = get_user_model()

class SendOTPView(APIView):
    def post(self, request):
        email = request.data.get('email')
        user = User.objects.filter(email=email).first()
        if not user:
            return Response({"errors":"user not found"}, status=status.HTTP_404_NOT_FOUND)

        if not can_resend(email):
            return Response({"errors":"Wait before resending OTP"}, status= status.HTTP_404_NOT_FOUND)
        if user.is_active:
            return Response({"errors":"Email already verified. No OTP needed"},
                            status=status.HTTP_400_BAD_REQUEST)
        otp = generate_otp()

        # Save otp to redis
        set_otp_in_redis(email,otp)

        set_resend_block(email)

        send_otp_email_task.delay(user.id, otp)

        return Response({"message":"OTP sent"}, status=status.HTTP_200_OK)
    
