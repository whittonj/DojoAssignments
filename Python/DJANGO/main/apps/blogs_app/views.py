from django.shortcuts import render, HttpResponse, redirect
# the index function is called when root is visited
def index(request):
  response = "placeholder to later display all the list of blogs"
  return HttpResponse(response)
def new(request):
  response = "placeholder for form to create new blog"
  return HttpResponse(response)
def create(request):
  response = "Create new blog"
  return HttpResponse(response)
def blog_number(request, blog_no):
  response = "Placeholder for blog number ", blog_no
  return HttpResponse(response)
def edit(request):
  response = "Edit this blog"
  return HttpResponse(response)
def destroy(request):
  response = "Delete blog"
  return redirect('/')
