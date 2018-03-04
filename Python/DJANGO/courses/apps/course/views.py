# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
from models import *

def index(request):
    return render(request, "course/index.html", { "course_list": course.objects.all() })

def create(request):
    if request.method == "POST":
        errors = course.objects.basic_validator(request.POST)
        request.session['errors'] =errors
        if len(errors):
            return redirect('/')
        else:
            course.objects.create(name=request.POST['name'], desc = request.POST['desc'])
            return redirect('/')
    else:
        return redirect('/')

def results(request, user_no):
    user_no = user_no
    return render(request, "course/results.html", { "course_info": course.objects.get(id=user_no) })

def destroy(request, user_no):
    d = course.objects.get(id=user_no)
    d.delete() # deletes that particular record
    return redirect('/')