from users.views.custom_jwt_tokenView import CustomTokenObtainPairView
from users.views.logutView import LogoutView
from users.views.register import UserRegisterView
from users.views.send_otp_view import SendOTPView
from users.views.verifyotp_view import VerifyOTPView
from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name="register"),
    path('send-otp/', SendOTPView.as_view(), name="otp_send"),
    path('verify-email/', VerifyOTPView.as_view(), name="verify_email"),
    path('login/', CustomTokenObtainPairView.as_view(), name="login"),
    path('token/refresh/', TokenRefreshView.as_view(), name="token_refresh"),
    path('logout/', LogoutView.as_view(), name="logout_view"),
]
