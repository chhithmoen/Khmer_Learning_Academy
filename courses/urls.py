from django.urls import path
from . import views


app_name = "courses"


urlpatterns = [

    # Course List (Home)
    path(
        "",
        views.course_list,
        name="course_list"
    ),


    # Course Detail
    path(
        "course/<int:pk>/",
        views.course_detail,
        name="course_detail"
    ),


    # Lesson Detail
    path(
        "lesson/<int:pk>/",
        views.lesson_detail,
        name="lesson_detail"
    ),

    path(
        "lesson/<int:pk>/complete/",
        views.complete_lesson,
        name="complete_lesson"
    ),


    # Student Dashboard
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


    # My Courses
    path(
        "my-courses/",
        views.my_courses,
        name="my_courses"
    ),

    path(
    "course/<int:pk>/enroll/",
    views.enroll_course,
    name="enroll_course"
    ),

]
