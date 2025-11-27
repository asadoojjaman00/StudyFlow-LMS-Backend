from rest_framework import serializers
from modules.models.module import Module


class ModuleInstructorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Module
        fields = '__all__'
        

class ModuleStudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Module
        fields = [
            'order',
            'title',
            'total_live_class_count',
            "total_assignment_count",
            'total_test_count',
            'start_day',
            'end_day',
            'is_active',
            'is_completed'
        ]
        read_only_fields = fields