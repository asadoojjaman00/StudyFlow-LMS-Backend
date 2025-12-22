from rest_framework import permissions



class IsInstructor(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'instructor'



class IsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'admin'



class IsCourseCreatorOrAdmin(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Readonly for everyone (GET, HEAD, OPTIONS)
        if request.method in permissions.SAFE_METHODS:
            return True
        # Modify only by creator or admin
        return obj.created_by == request.user or request.user.role == 'admin'



class IsEnrolledStudent(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return obj.enrolled_students.filter(id=request.user.id).exists()
        return False