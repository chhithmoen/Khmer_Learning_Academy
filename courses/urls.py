from django.urls import path
from . import views


app_name = "courses"


urlpatterns = [

    # Course List Home Page
    path(
        "",
        views.course_list,
        name="course_list"
    ),


    # User Dashboard
    path(
        "dashboard/",
        views.dashboard,
        name="dashboard"
    ),


    # User Profile
    path(
        "profile/",
        views.profile,
        name="profile"
    ),


    # My Enrolled Courses
    path(
        "my-courses/",
        views.my_courses,
        name="my_courses"
    ),


    # Enroll Course
    path(
        "enroll/<int:pk>/",
        views.enroll_course,
        name="enroll_course"
    ),


    # Course Detail
    path(
        "<int:pk>/",
        views.course_detail,
        name="course_detail"
    ),


    # Lesson Detail
    path(
        "<int:course_pk>/lesson/<int:lesson_pk>/",
        views.lesson_detail,
        name="lesson_detail"
    ),

    path(
    "course/<int:pk>/enroll/",
    views.enroll_course,
    name="enroll_course",
    ),

    path(
    "lesson/<int:course_pk>/<int:lesson_pk>/complete/",
    views.complete_lesson,
    name="complete_lesson",
),

]