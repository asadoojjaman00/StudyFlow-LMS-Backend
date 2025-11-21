from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from common.utils.permissions import IsInstructorOrReadonly

from modules.models.module import Module

from modules.serializers.module import(
    ModuleInstructorSerializer,
    ModuleStudentSerializer
)


class InstructorModuleView(APIView):

    permission_classes = [IsInstructorOrReadonly]

    def get_serializer_class(self):
        user = self.request.user
        if not user.is_authenticated:
            return ModuleStudentSerializer
        if user.role == 'instructor':
            return ModuleInstructorSerializer
        return ModuleStudentSerializer
        


    def get(self, request):
        module = Module.objects.all()
        serializer_class = self.get_serializer_class()
        serializer = serializer_class(module, many = True, context={'request':request})
        return Response(serializer.data)
        
    def post(self, request):
        serializer_class = self.get_serializer_class()
        serializer = serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def put(self, request, *args, **kwargs):
        module_id = kwargs.get('id')


        try:
            module = Module.objects.get(id = module_id)
        except Module.DoesNotExist:
            return Response(
                {'errors': 'Module not found'},
                status=status.HTTP_404_NOT_FOUND
            )
        
        serializer_class = self.get_serializer_class()
        serializer = serializer_class(module, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_200_OK
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
