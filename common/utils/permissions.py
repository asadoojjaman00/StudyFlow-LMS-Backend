from rest_framework.permissions import BasePermission


class IsInstructor(BasePermission):
    message = "Only instructor can access this"

    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'instructor'
    
class IsStudent(BasePermission):
    message = "Only student can access this"

    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'student'
    