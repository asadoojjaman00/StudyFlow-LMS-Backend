from rest_framework import permissions


class IsInstructorOrReadonly(permissions.BasePermission):
    message = "Only instructor can access this"

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_authenticated and request.user.role == 'instructor'
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.created_by == request.user
        
