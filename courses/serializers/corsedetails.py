from rest_framework import serializers
from courses.models.coursedetails import CourseDetails


class CourseDetailInstructorSerializer(serializers.ModelSerializer):
    course_title = serializers.CharField(source='course.title', read_only=True)
    course_description = serializers.CharField(source='course.description', read_only=True)

    class Meta:
        model = CourseDetails
        fields = [
            'course_title',
            'course_description',
            'demo_class_video',
            'price',
            'discount_price',
            'total_live_classes',
            'total_projects',
            'created_at',
            'updated_at',
        ]
        read_only_fields = [
            'course_title',
            'course_description',
            'created_at',
            'updated_at'
        ]

class CourseDetailStudentSerializer(serializers.ModelSerializer):
    course_title = serializers.CharField(source='course.title', read_only=True)
    course_description = serializers.CharField(source='course.description', read_only=True)

    class Meta:
        model = CourseDetails
        fields = [
            'course_title',
            'course_description',
            'demo_class_video',
            'price',
            'discount_price',
            'total_live_classes',
            'total_projects',
        ]
        read_only_fields = fields