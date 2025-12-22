from rest_framework import serializers
from courses.models.coursemodel import Course


class CourseSerializer(serializers.ModelSerializer):
    total_course_module = serializers.SerializerMethodField()
    total_projects = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = "__all__"

    def get_total_course_module(self, obj):
        return 0  # later: obj.modules.filter(type="live").count()

    def get_total_projects(self, obj):
        return 0
