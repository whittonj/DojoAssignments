# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
from models import *
from django.contrib import messages
import bcrypt

#, { "user_list": users.objects.all() }

def index(request):
    #request.session['counter'] = 1
    return render(request, "login/index.html")

def create(request):
    if request.method == "POST":
        errors = user.objects.basic_validator(request.POST)
        if len(errors):
            for tag, error in errors.iteritems():
                messages.error(request, error, extra_tags=tag)
            return redirect('/')
        else:
            pass_hash = bcrypt.hashpw(request.POST['pass'].encode(), bcrypt.gensalt())
            user.objects.create(name=request.POST['name'], alias = request.POST['alias'],email_address = request.POST['email_address'], password=pass_hash  )
            #request.session['name'] = request.POST['first_name'] 
            return redirect('/register', { "user_data": user.objects.get(email_address = request.POST['email_address']) })
    else:
        return redirect('/')

def results(request):
    request.session['user_data'] =context
    return render(request, "login/results.html")

def register(request):
    return render(request, "login/register.html")

def login(request):
    errors = user.objects.login_try(request.POST)  
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
            return redirect('/')        
    else:
        errors = user.objects.pw_match(request.POST)
        context = {
            "user_data": user.objects.get(email_address = request.POST['login_address'])
        }

        return render(request, "login/results.html", context)