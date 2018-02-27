# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect

def index(request):
    request.session['counter'] = 1
    return render(request, "survey/index.html")

def create(request):
    if request.method == "POST":
        print "*"*50
        print request.POST
        request.session['counter'] = request.session['counter'] + 1
        request.session['name'] = request.POST['name'] 
        request.session['location'] = request.POST['location']
        request.session['comment'] = request.POST['comment']
        return redirect(results)
    else:
        return redirect('/')

def results(request):
     return render(request, "survey/results.html")
