from rest_framework import generics
from common.utils.permissions import IsAdmin, IsInstructor, IsCourseCreatorOrAdmin
from courses.models.coursemodel import Course
from courses.serializers.courseserializers import CourseSerializer


# --------Course create View(admin & instructor only)-------

class CourseCreateView(generics.CreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAdmin | IsInstructor]
    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

# --------Course update View(admin & Course creator (instructor) only)-------


class CourseUpdateView(generics.UpdateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsCourseCreatorOrAdmin]
    lookup_field = 'id'

# --------Course delete View(admin & Course creator (instructor) only)-------


class CourseDeleteView(generics.DestroyAPIView):
    queryset = Course.objects.all()
    permission_classes = [IsCourseCreatorOrAdmin]
    lookup_field = 'id'