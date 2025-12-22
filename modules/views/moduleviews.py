from rest_framework import generics
from modules.models.module import Module
from modules.serializers.moduleserializer import ModuleSerializer
from common.utils.permissions import IsCourseCreatorOrAdmin


# -------------------Module Create View (Access : course creator | admin)-----------
class ModuleCreateView(generics.CreateAPIView):
    queryset = Module.objects.all()
    serializer_class = ModuleSerializer
    permission_classes = [IsCourseCreatorOrAdmin]


# -------------------Module Update View (Access : course creator | admin)-----------
class ModuleUpdateView(generics.UpdateAPIView):
    queryset = Module.objects.all()
    serializer_class = ModuleSerializer
    permission_classes = [IsCourseCreatorOrAdmin]
    lookup_field = "id"


# -------------------Module Delete View (Access : course creator | admin)-----------
class ModuleDeleteView(generics.DestroyAPIView):
    queryset = Module.objects.all()
    permission_classes = [IsCourseCreatorOrAdmin]
    lookup_field = "id"
