from rest_framework import serializers
from courses.models import Category

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields  = '__all__'
        read_only_fields = ['id','slug','created_at', 'updated_at']