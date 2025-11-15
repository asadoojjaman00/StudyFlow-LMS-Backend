from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from common.utils.permissions import IsInstructor


from serializers.course import CourseSerializer



class CourseView(APIView):
    permission_classes = [IsAuthenticated,IsInstructor]

    def post(self, request):
        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(instructor = request.user)
            
            return Response(
                {'message':'Course created Successfully'},
                status=status.HTTP_201_CREATED
            )
        return Response(
            {"errors":serializer.errors},
            status=status.HTTP_400_BAD_REQUEST
        )