# theater-scholl-app/core/admin.py

from django.contrib import admin
from .models import TheatricalPerformance, Course, Instructor, Student, Review

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('student', 'text', 'approved')
    list_filter = ('approved',)
    actions = ['approve_reviews']

    def approve_reviews(self, request, queryset):
        queryset.update(approved=True)

admin.site.register(TheatricalPerformance)
admin.site.register(Course)
admin.site.register(Instructor)
admin.site.register(Student)
admin.site.register(Review, ReviewAdmin)
