from django.shortcuts import render, get_object_or_404
from .models import Course, Lesson


def course_list(request):
    courses = Course.objects.all()

    return render(
        request,
        "courses/course_list.html",
        {
            "courses": courses,
        }
    )


def course_detail(request, pk):
    course = get_object_or_404(Course, pk=pk)

    lessons = course.lessons.all()

    return render(
        request,
        "courses/course_detail.html",
        {
            "course": course,
            "lessons": lessons,
        }
    )


def lesson_detail(request, course_pk, lesson_pk):

    course = get_object_or_404(
        Course,
        pk=course_pk
    )

    lesson = get_object_or_404(
        Lesson,
        pk=lesson_pk,
        course=course
    )

    lessons = course.lessons.all()

    return render(
        request,
        "courses/lesson_detail.html",
        {
            "course": course,
            "lesson": lesson,
            "lessons": lessons,
        },
    )