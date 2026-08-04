from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone

from .models import Course, Lesson, LessonProgress

from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from .models import Course, Lesson, Enrollment


# Home / Course List
def course_list(request):

    courses = Course.objects.all()

    context = {
        "courses": courses
    }

    return render(
        request,
        "courses/course_list.html",
        context
    )


# Course Detail
def course_detail(request, pk):

    course = get_object_or_404(
        Course,
        id=pk
    )

    lessons = course.lessons.all()

    enrolled = False

    if request.user.is_authenticated:
        enrolled = Enrollment.objects.filter(
            student=request.user,
            course=course
        ).exists()


    context = {
        "course": course,
        "lessons": lessons,
        "enrolled": enrolled,
    }


    return render(
        request,
        "courses/course_detail.html",
        context
    )

# Lesson Detail
def lesson_detail(request, pk):

    lesson = get_object_or_404(
        Lesson,
        id=pk
    )

    progress = None
    if request.user.is_authenticated:
        progress = LessonProgress.objects.filter(
            student=request.user,
            lesson=lesson,
        ).first()

    context = {
        "course": lesson.course,
        "lesson": lesson,
        "lessons": lesson.course.lessons.all(),
        "progress": progress,
    }

    return render(
        request,
        "courses/lesson_detail.html",
        context
    )


@login_required
def complete_lesson(request, pk):
    """Mark a lesson as completed for the current user."""
    if request.method != "POST":
        return redirect("courses:lesson_detail", pk=pk)

    lesson = get_object_or_404(Lesson, id=pk)
    progress, _ = LessonProgress.objects.get_or_create(
        student=request.user,
        lesson=lesson,
    )

    if not progress.completed:
        progress.completed = True
        progress.completed_at = timezone.now()
        progress.save(update_fields=["completed", "completed_at"])

    return redirect("courses:lesson_detail", pk=lesson.pk)


# Dashboard
def dashboard(request):

    return render(
        request,
        "dashboard.html"
    )


# Profile
def profile(request):

    return render(
        request,
        "profile.html"
    )


# My Courses
@login_required
def my_courses(request):

    enrollments = Enrollment.objects.filter(
        student=request.user
    )

    courses = [
        enrollment.course
        for enrollment in enrollments
    ]


    context = {
        "courses": courses
    }


    return render(
        request,
        "courses/my_courses.html",
        context
    )

@login_required
def enroll_course(request, pk):

    course = get_object_or_404(
        Course,
        id=pk
    )


    Enrollment.objects.get_or_create(
        student=request.user,
        course=course
    )


    return redirect(
        "courses:course_detail",
        pk=course.id
    )
