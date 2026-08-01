from django.contrib import admin
from .models import Course, Lesson, Enrollment

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "created_at",
    )


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "course",
    )

    list_filter = (
        "course",
    )

    ordering = (
        "course",
    )


admin.site.register(Enrollment)

from .models import (
    Course,
    Lesson,
    Enrollment,
    LessonProgress,
)

admin.site.register(LessonProgress)