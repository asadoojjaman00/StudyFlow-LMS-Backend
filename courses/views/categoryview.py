from rest_framework import generics

from courses.serializers.categoryserializer import CategorySerializer
from courses.models import Category

from common.utils.permissions import IsAdmin




class CategoryListCreateView(generics.ListCreateAPIView):

    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdmin]


class CategoryRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdmin]
  


