from django.contrib import admin
from .models import Category, Course, Enrollment
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active', 'created_at', 'updated_at')
    prepopulated_fields = {'slug':('name',)}

class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_published', 'created_by', 'price')
    prepopulated_fields = {'slug':('title',)}

admin.site.register(Category,CategoryAdmin)
admin.site.register(Course,CourseAdmin)
admin.site.register(Enrollment)

