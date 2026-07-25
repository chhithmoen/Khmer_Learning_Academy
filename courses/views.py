from django.shortcuts import render, get_object_or_404

from .models import Course



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




def course_detail(request, id):

    course = get_object_or_404(
        Course,
        id=id
    )


    context = {
        "course": course
    }


    return render(
        request,
        "courses/course_detail.html",
        context
    )