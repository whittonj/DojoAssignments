# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime
from django.utils.crypto import get_random_string, random

def index(request):
    current_list = []
    request.session['where_to'] = []
    current_list.append(["Farm", 10, 20])
    current_list.append(["Cave", 5, 10])
    current_list.append(["House", 2, 5])
    current_list.append(["Casino", -50, 50])
    request.session['workplace'] = current_list
    return render(request, "ninja/index.html")

def create(request):
    if request.method == "POST":
        new_str= request.session['goto']+", "+ request.POST['goto'] 
        low = int(request.POST['low'])
        high= int(request.POST['high'])
        request.session['goto'] = new_str 
        request.session['new_gold'] = random.randint( low, high )
        request.session['gold'] = request.session['gold'] + request.session['new_gold']
        return redirect('/results')

def results(request):
    #What?
    return redirect('/')