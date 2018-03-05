# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
from .models import *
from django.contrib import messages
import bcrypt

#, { "user_list": users.objects.all() } { "user_data": user.objects.get(email_address = request.POST['email_address']) }

def newbook(request):
    if request.method == "POST":
        if  (len(author.objects.filter(name = request.POST['author_name']))>0):
            print "try again"
            return redirect('/books/add')
        else:
            author.objects.create(name =request.POST['author_name'])
            auth_id = author.objects.get(name=request.POST['author_name'])
            book.objects.create(name=request.POST['book_name'])
            book_id = book.objects.get(name=request.POST['book_name']).id
            review.objects.create(rating=request.POST['rating'], review_txt = request.POST['review'], book_id=book_id, user_id = request.session['user_id'])
        #request.session['name'] = request.POST['first_name'] 
        return redirect('/')
    else:
        return redirect('/')

def create_book(request):
    context = {
        "dropdown": author.objects.all()
    }
    return render (request, "review/create.html", context )