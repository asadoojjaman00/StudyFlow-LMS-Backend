from rest_framework import serializers
from lessons.models.lesson import Lesson


class StudentLessonSerializer(serializers.ModelSerializer):


    class Meta:
        model = Lesson
        fields = ['type','title','lesson_link','description', 'start_date', 'end_date']
        read_only_fields = fields



class InstructorLessonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lesson
        fields = '__all__'