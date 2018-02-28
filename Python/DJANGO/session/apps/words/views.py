# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime
# the index function is called when root is visited
current_list = []
def index(request):
    #why not
    return render(request, "words/index.html")

def create(request):
    if request.method == "POST":
        time =  strftime("%Y-%m-%d %H:%M %p", gmtime())
        request.session['time'] = time
        request.session['text'] = request.POST['text'] 
        request.session['color'] = request.POST['color']
        if 'big' not in request.POST:
            request.session['big'] = "small"
            return redirect(results)
        else:
            request.session['big'] = request.POST['big']
            return redirect(results)
    else:
        return redirect('/')

def results(request):
    newstr = request.session['text'] 
    color = request.session['color']
    size = request.session['big']
    current_list.append([newstr,color,size])
    request.session['list'] = current_list
    return redirect('/')
    #return render(request, "words/results.html")