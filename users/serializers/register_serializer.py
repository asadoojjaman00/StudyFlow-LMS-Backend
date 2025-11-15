from users.models.user_model import User
from rest_framework import serializers



class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['id','full_name', 'email', 'phone_number', 'password']
        
    def create(self, validated_data):
        return User.objects.create_user(
            full_name = validated_data['full_name'],
            email = validated_data['email'],
            phone_number = validated_data['phone_number'],
            password = validated_data['password']   
        )

