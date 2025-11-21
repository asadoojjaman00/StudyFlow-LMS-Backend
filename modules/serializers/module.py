from rest_framework import serializers
from modules.models.module import Module


class ModuleInstructorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Module
        fields = '__all__'
        read_only_fields= [
            'created_at',
            'updated_at'
        ]

class ModuleStudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Module
        fields = [
            'order'
            'title',
            'total_live_class_count',
            "total_assignment_count",
            'total_test_count',
            'start_day',
            'end_day',
            'is_unlocked'
        ]
        read_only_fields = fields