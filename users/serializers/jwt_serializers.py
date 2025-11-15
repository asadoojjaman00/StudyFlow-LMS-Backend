from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # extra user data:
        token['full_name'] = user.full_name
        token['email'] = user.email
        token['role'] = user.role 
    
        return token