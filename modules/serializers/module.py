from rest_framework import serializers



from modules.models.module import Module


class ModuleSerializerForInstructor(serializers.ModelSerializer):


    class Meta:
        model = Module
        fields = '__all__'
        