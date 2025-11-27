from rest_framework import permissions


# permission helper function : 

def get_course_from_obj(obj):
    if hasattr(obj, "course"):
        return obj.course
    elif hasattr(obj, "module"):
        return obj.module.course
    else:
        return obj



# course creator check and allow or deny permission 

class IsCourseCreatorOrReadonly(permissions.BasePermission):
    message = "Only course creator can modify this content"

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_authenticated and request.user.role == 'instructor'

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        
        course = get_course_from_obj(obj)
        return course.created_by == request.user


# course instructor check and allow or deny permission

class IsInstructorOfCourse(permissions.BasePermission):

    message = "Only course instructor can access this"

    def has_object_permission(self, request, view, obj):
        user = request.user

        if not user.is_authenticated:
            return False
        
        course = get_course_from_obj(obj)
        return user in course.instructors.all()
    


# course enrolled student check and allow or deny permission

class IsEnrolledStudent(permissions.BasePermission):

    message = "Only enrolled student access this course"

    def has_object_permission(self, request, view, obj):
        user = request.user

        if not user.is_authenticated:
            return False
        
        course = get_course_from_obj(obj)
        return course.enrollments.filter(student=user).exists()