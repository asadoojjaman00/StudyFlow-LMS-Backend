from rest_framework import serializers
from courses.models.course import Course
from django.urls import reverse

class CourseInstructorSerializer(serializers.ModelSerializer):
    detail_url = serializers.SerializerMethodField()
    class Meta:
        model = Course
        fields = '__all__'
        read_only_fields = ['slug', 'total_enrolled','thumbnail']

    def get_detail_url(self, obj):
        request = self.context.get('request')
        if request is None:
            return None
        
        try:
            return request.build_absolute_uri(reverse('course-detail', kwargs={'pk':obj.pk}))
        except:
            return f"/course/{obj.pk}/"
class CourseStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = [
            'id',
            'title',
            'type',
            'category',
            'thumbnail',
            'total_enrolled',
            'is_published'
        ]
        read_only_fields = fields
