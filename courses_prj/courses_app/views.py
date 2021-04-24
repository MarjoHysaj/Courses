from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import *

def index(request):
    course = Course.objects.all()
    desc = Desc.objects.all()
    context = {
        'courses': course,
        'desc': desc
    }
    return render(request, "index.html", context)

def create(request):
    errors = Course.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key,value in errors.items():
            messages.error(request,value)
        return redirect('/courses')
    else:
        desc = Desc.objects.create(
            desc = request.POST['desc']
        )
        course = Course.objects.create(
            name = request.POST['name'],
            desc_id = desc.id
        )
        messages.success(request, "Blog successfully updated")
        return redirect("/courses")

def show(request, id):
    course = Course.objects.get(id=id)
    context = {
        'course' : course,
        'desc' : Course.objects.get(desc_id=id)
    }
    return render(request, "index.html", context)

def edit(request, id):
    course = Course.objects.get(id=id)
    desc = Course.objects.get(desc_id=id)
    context = {
        'course' : course,
        'desc' : desc
    }
    return render(request, "remove.html", context)

def destroy(request, id):
    course = Course.objects.get(id=id)
    course.delete()
    return redirect('/courses')

def commentshow(request, id):
    course = Course.objects.get(id=id)
    context = {
        'course' : course,
        'comments' : Comment.objects.all()
    }
    return render(request, "comment.html", context)

def commentcreate(request, id):
    course = Course.objects.get(id=id)
    comment = Comment.objects.create(text=request.POST['text'], course=course)
    return redirect('/courses/comment/'+str(course.id))