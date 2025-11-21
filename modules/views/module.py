from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from common.utils.permissions import IsInstructorOrReadonly

from modules.serializers.module import ModuleSerializerForInstructor


class InstructorModuleView(APIView):...
