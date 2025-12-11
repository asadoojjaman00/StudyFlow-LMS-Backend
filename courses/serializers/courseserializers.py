from rest_framework import serializers
from courses.models.course import Course
from courses.models.category import Category
from users.models.User_model import User

from django.utils.text import slugify


# =======================================
# course serializer for : post/put/delete
# =======================================


# Course create serializer

class CourseCreateUpdateSerializer(serializers.ModelSerializer):

    # for category selection 
    
    category = serializers.SlugRelatedField(
        slug_field = 'slug',
        queryset = Category.objects.filter(is_active=True)
    )


    # for instructors selection 
    
    instructors = serializers.PrimaryKeyRelatedField(
        many = True,
        queryset = User.objects.filter(role='instructor'),
        required = False
    )


    class Meta:
        model = Course
        fields = '__all__'
        read_only_fields = ['uuid','slug', 'total_enrolled', 'created_at', 'updated_at']

    # course creator validation

    def create(self, validated_data):
        request = self.context.get('request')
        if request and hasattr(request, 'user'):
            validated_data['created_by'] = request.user
        return super().create(validated_data)
    
    # slug validation for put request

    def update(self, instance, validated_data):
        if 'title' in validated_data:
            base = slugify(validated_data['title'])
            slug = base
            count += 1
            while Course.objects.filter(slug=slug).exclude(id=instance.id).exists():
                slug = f"{base}-{count}"
                count += 1

            instance.slug = slug
        return super().update(instance,validated_data) 

    # paid type validation

    def validate(self, data):
        if data.get('type') == 'paid' and not data.get('price'):
            raise serializers.ValidationError('paid course must have price')
        return data