from rest_framework_simplejwt.views import TokenObtainPairView
from users.serializers.jwt_serializers import CustomTokenObtainPairSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from django.contrib.auth import get_user_model

User = get_user_model()

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
    permission_classes = [AllowAny]

    def post(self,request, *args, **kwargs):
        email = request.data.get('email')
        
        user = User.objects.filter(email = email).first()

        if user is None:
            return Response({"errors":"Invalid email"}, status=status.HTTP_404_NOT_FOUND)
        
        if not user.is_active:
            return Response(
                {"errors":"Your account not email verified please verify your email first",
                 "redirect_url": f"/verify-email?email={email}"
                },

                status=status.HTTP_403_FORBIDDEN
            )
        return super().post(request, *args, **kwargs)