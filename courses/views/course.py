from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from common.utils.permissions import IsInstructor


from serializers.course import CourseSerializer
from models.course import Course



# only instructor can create a post and update own post view: 

class CourseCreateAndUpdate(APIView):

    permission_classes = [IsAuthenticated,IsInstructor]


    def post(self, request):
        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(created_by = request.user)
            
            return Response(
                {'message':'Course created Successfully'},
                status=status.HTTP_201_CREATED
            )
        return Response(
            {"errors":serializer.errors},
            status=status.HTTP_400_BAD_REQUEST
        )
    


    # only :created_by user can do this 
    def put(self, request):
        course_id  = request.data.get("id")
        if not course_id:
            return Response(
                {"errors":"id field is required for updating course item"},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            course = Course.objects.get(id=course_id)
        except Course.DoesNotExist:
            return Response(
                {"errors":"Course not found"},
                status=status.HTTP_404_NOT_FOUND
            )


        if course.created_by != request.user:
            return Response(
                {"errors": "Your are not allowed to update this course"},
                status=status.HTTP_403_FORBIDDEN
            )

        serializer = CourseSerializer(course, data=request.data, partial =True)

        if serializer.is_valid():
            serializer.save()
            return Response(
                {'message':'Course updated successfully'},
                status=status.HTTP_200_OK
            )
        return Response(
            {'errors':serializer.errors},
            status=status.HTTP_400_BAD_REQUEST
        )