from django.urls import path
from .views.course import CourseViewAndCreate
from .views.coursedetails import CourseDetailViewAndCreate

urlpatterns = [
    path('course/', CourseViewAndCreate.as_view(), name='course-view-create'),
    path('course/<int:pk>/', CourseDetailViewAndCreate.as_view(), name='course-detail-view-create-update')
]

