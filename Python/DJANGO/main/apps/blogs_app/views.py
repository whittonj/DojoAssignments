from django.shortcuts import render, HttpResponse, redirect
# the index function is called when root is visited
def index(request):
  response = "placeholder to later display all the list of blogs"
  return HttpResponse(response)
def new(request):
  response = "placeholder for form to create new blog"
  return HttpResponse(response)
def create(request):
  response = "redirect for now"
  return redirect('/')
def blog_number(request):
  response = "Placeholder for blog number"
  return HttpResponse(response)
