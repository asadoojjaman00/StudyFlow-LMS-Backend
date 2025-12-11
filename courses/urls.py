from django.urls import path
from courses.views.categoryview import CategoryListCreateView, CategoryRetrieveUpdateDestroyView
from courses.views.courseviews import(
    CourseCreateView,
    CourseUpdateView,
    CourseDeleteView
)
urlpatterns = [
    path('categories/', CategoryListCreateView.as_view(), name='category-list-create'),
    path('categories/<int:pk>/', CategoryRetrieveUpdateDestroyView.as_view(), name='category-detail'),
    path('course/', CourseCreateView.as_view(), name='course-create'),
    path('course/<int:id>/', CourseUpdateView.as_view(), name="course-update"),
    path('course/<int:id>/', CourseDeleteView.as_view(), name="course-delete"),
]