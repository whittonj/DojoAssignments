# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime

def index(request):
    request.session['purchase_no'] =0
    current_list = []
    current_list.append(["Hat", 17.95, 1])
    current_list.append(["Shirt", 12.92, 2])
    current_list.append(["Sunnies", 9.05, 3])
    request.session['items'] = current_list
    return render(request, "store/index.html")

def create(request):
    if request.method == "POST":
        time =  strftime("%Y-%m-%d %H:%M %p", gmtime())
        request.session['time'] = time
        request.session['purchase_no'] = request.session['purchase_no'] + 1
        request.session['product_id'] = request.POST['product_id'] 
        request.session['quantity'] = request.POST['quantity']
        if request.session['product_id'] == "1":
            request.session['product'] = "Hat"
            request.session['price'] = 17.95
        if request.session['product_id'] == "2":
            request.session['product'] = "Shirt"
            request.session['price'] = 12.92
        if request.session['product_id'] == "3":
            request.session['product'] = "Sunnies"
            request.session['price'] = 9.05
        request.session['total'] = float(request.session['price']) * float(request.session['quantity'])
        return redirect('/results')

def results(request):
    newstr = request.session['product_id'] 
    qty = request.session['quantity']
    return render(request, "store/results.html")