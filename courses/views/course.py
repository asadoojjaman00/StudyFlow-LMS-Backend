from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from common.utils.permissions import IsInstructorOrReadonly


from courses.serializers.course import (
    CourseInstructorSerializer,
    CourseStudentSerializer
)
from courses.models.course import Course





class CourseViewAndCreate(APIView):

    permission_classes = [IsInstructorOrReadonly]

    def get_serializer_class(self):
        user = self.request.user
        if not user.is_authenticated:
            return CourseStudentSerializer
        if user.role == 'instructor':
            return CourseInstructorSerializer
        else:
            return CourseStudentSerializer
        

    def get(self, request, *args, **kwargs):
        courses = Course.objects.all()
        serializer_class = self.get_serializer_class()
        serializer = serializer_class(courses, many=True, context={'request': request})
        return Response(serializer.data)
    
    def post(self, request):
        serializer_class = self.get_serializer_class()
        serializer = serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save(created_by = request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, *args, **kwargs):
        course_id = kwargs.get('id')

        try:
            course = Course.objects.get(id=course_id)
        except Course.DoesNotExist:
            return Response(
                {'message':'Course not found'}
            )
        serializer_class = self.get_serializer_class()
        serializer = serializer_class(course, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_200_OK
            )
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)






