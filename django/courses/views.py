from django.shortcuts import render

from .models import Course

def courses(request):
    courses = Course.objects.all()
    return render(request, 'courses/course_list.html', {'courses': courses})
