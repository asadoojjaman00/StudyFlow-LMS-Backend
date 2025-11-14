
from rest_framework.views import APIView
from rest_framework import status, permissions
from rest_framework.response import Response

from users.serializers.register_serializer import UserRegisterSerializer

class  UserRegisterView(APIView):

    permission_classes = [permissions.AllowAny]

    def post(self ,request):
        serializer = UserRegisterSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "message":"Account Successfully Created",
                    "data":serializer.data
                },
                status= status.HTTP_201_CREATED
            )
        return Response(
                {
                    "message":"Validation Failed",
                    "errors":serializer.errors
                },
                status= status.HTTP_400_BAD_REQUEST
            )




