# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
from models import *
from django.contrib import messages
import bcrypt

#, { "user_list": users.objects.all() }

def index(request):
    request.session['counter'] = 1
    return render(request, "user_login/index.html")

def create(request):
    if request.method == "POST":
        errors = users.objects.basic_validator(request.POST)
        if len(errors):
            for tag, error in errors.iteritems():
                messages.error(request, error, extra_tags=tag)
            return redirect('/')
        else:
            pass_hash = bcrypt.hashpw(request.POST['pass'].encode(), bcrypt.gensalt())
            users.objects.create(first_name=request.POST['first_name'], last_name = request.POST['last_name'],email_address = request.POST['email_address'], password=pass_hash  )
            request.session['name'] = request.POST['first_name'] 
            return redirect('/results', { "user_data": users.objects.get(email_address = request.POST['email_address']) })
            #should go to separate form awith different fields passes- this data not in DB yet to pass
    else:
        return redirect('/')

def results(request):
    return render(request, "user_login/results.html")

def login(request):
    errors = users.objects.login_try(request.POST)  
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
            return redirect('/')        
    else:
        errors = users.objects.pw_match(request.POST)
        return render(request, "user_login/results.html",  { "user_data": users.objects.get(email_address = request.POST['login_address']) } )