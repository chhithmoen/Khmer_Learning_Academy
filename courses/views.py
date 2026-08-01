from django.shortcuts import render, get_object_or_404
from .models import Course, Lesson
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Course, Lesson, Enrollment
from django.shortcuts import redirect
from django.shortcuts import redirect, get_object_or_404
from .models import Course, Lesson, Enrollment

@login_required
def enroll_course(request, pk):
    course = get_object_or_404(Course, pk=pk)

    Enrollment.objects.get_or_create(
        student=request.user,
        course=course
    )

    return redirect("courses:course_detail", pk=pk)

@login_required
def dashboard(request):
    return render(
        request,
        "courses/dashboard.html"
    )


@login_required
def profile(request):
    return render(
        request,
        "courses/profile.html"
    )


@login_required
def my_courses(request):

    enrollments = Enrollment.objects.filter(
        student=request.user
    )

    courses = [
        enrollment.course
        for enrollment in enrollments
    ]

    return render(
        request,
        "courses/my_courses.html",
        {
            "courses": courses
        }
    )


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

@login_required
def enroll_course(request, pk):

    course = get_object_or_404(
        Course,
        pk=pk
    )

    Enrollment.objects.get_or_create(
        student=request.user,
        course=course
    )

    return redirect(
    "courses:my_courses"
    )
from django.utils import timezone
from .models import (
    Course,
    Lesson,
    Enrollment,
    LessonProgress,
)

@login_required
def complete_lesson(request, course_pk, lesson_pk):
    lesson = get_object_or_404(
        Lesson,
        pk=lesson_pk,
        course_id=course_pk
    )

    progress, created = LessonProgress.objects.get_or_create(
        student=request.user,
        lesson=lesson
    )

    progress.completed = True
    progress.completed_at = timezone.now()
    progress.save()

    return redirect(
        "courses:lesson_detail",
        course_pk=course_pk,
        lesson_pk=lesson_pk,
    )