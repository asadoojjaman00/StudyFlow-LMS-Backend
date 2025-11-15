from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.core.cache import cache
from django.contrib.auth import get_user_model


User = get_user_model()

class VerifyOTPView(APIView):
    
    def post(self, request):

        email = request.data.get('email')
        otp_input = request.data.get('otp')

        otp_stored = cache.get(f"otp:{email}")

        if otp_stored is None:
            return Response({"errors":"OTP expired or not found"}, status=status.HTTP_400_BAD_REQUEST)
    
        if otp_stored != otp_input:
            return Response({"errors": "Invalid OTP"}, status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.get(email=email)
        user.is_active = True
        user.save()

        cache.delete(f"otp:{email}")

        return Response({"message": "Email Verified"}, status=status.HTTP_200_OK)
    