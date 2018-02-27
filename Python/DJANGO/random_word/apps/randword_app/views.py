# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string 
  # the index function is called when root is visited
def index(request):
    response = "Hello, I am your random word placeholder"
    word = get_random_string(length=14)
    request.session['counter'] = request.session['counter']+ 1
    context = {
        "randword": word
    }
    return render(request,'randword_app/index.html', context)

def reset(request):
    request.session['counter'] = 0
    return redirect('/')
# Create your views here.
