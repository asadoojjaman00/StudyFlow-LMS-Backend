from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from courses.models.coursedetails import CourseDetails

from common.utils.permissions import (
    IsInstructorOfCourse,
    IsEnrolledStudent,
    IsCourseCreatorOrReadonly
)




from courses.serializers.corsedetails import(
    CourseDetailInstructorSerializer,
    CourseDetailStudentSerializer
)

class CourseDetailViewAndCreate(APIView):
    permission_classes = [IsInstructorOfCourse,
    IsEnrolledStudent,
    IsCourseCreatorOrReadonly
]

    def get_serializer_class(self,user):
        user = self.request.user 

        if not user.is_authenticated:
            return CourseDetailStudentSerializer
        if user.role == 'instructor':
            return CourseDetailInstructorSerializer
        else:
            return CourseDetailStudentSerializer
        



    def get(self, request, pk=None):
        serializer_class = self.get_serializer_class(request.user)
        if pk:
            try:
                detail = CourseDetails.objects.get(pk=pk)
            except CourseDetails.DoesNotExist:
                return Response(
                    {'detail':'CourseDetails not found'},
                    status=status.HTTP_404_NOT_FOUND
                )
            serializer = serializer_class(detail, context={'request':request})
            return Response(
                serializer.data,
                status=status.HTTP_200_OK
            )
        return Response(
            {'errors':'Course id/pk required'},
            status=status.HTTP_400_BAD_REQUEST
        )
    
    def post(self, request):
        serializer_class = self.get_serializer_class(request.user)
        serializer = serializer_class(data=request.data, context={'request':request})
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
    
    def put(self, request, pk=None):
        if not pk:
            return Response(
                {'errors':'CourseDetails pk required for update'},
                status=status.HTTP_400_BAD_REQUEST
             )
        try:
            detail = CourseDetails.objects.get(pk=pk)
        except CourseDetails.DoesNotExist:
            return Response(
                {'errors':'CourseDetails not found'},
                status=status.HTTP_404_NOT_FOUND
            )
        serializer_class = self.get_serializer_class(request.user)
        serializer = serializer_class(detail, data=request.data, partial=True, context={'request':request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )