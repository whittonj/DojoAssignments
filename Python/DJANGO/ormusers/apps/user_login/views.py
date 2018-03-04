# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
from models import *

def index(request):
    request.session['counter'] = 1
    return render(request, "user_login/index.html", { "user_list": users.objects.all() })

def new(request):
   return render(request, "user_login/create.html")

def create(request):
    if request.method == "POST":
        users.objects.create(first_name=request.POST['first_name'], last_name = request.POST['last_name'],email_address = request.POST['email_address'], age=request.POST['age']   )
        request.session['name'] = request.POST['first_name'] 
        return redirect('/')
    else:
        return redirect('/')

def results(request, user_no):
    user_no = user_no
    return render(request, "user_login/results.html", { "user_info": users.objects.get(id=user_no) })

def edit(request, user_no):
    user_no = user_no
    return render(request, "user_login/edit.html", { "user_info": users.objects.get(id=user_no) },)

def update(request, user_no):
    user_no=user_no
    u_user=users.objects.get(id=user_no)
    u_user.first_name = request.POST['first_name']
    u_user.last_name = request.POST['last_name']
    u_user.email_address = request.POST['email_address']
    u_user.age = request.POST['age']
    u_user.save()
    return redirect('/')