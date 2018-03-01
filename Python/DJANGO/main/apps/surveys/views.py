from django.shortcuts import render, HttpResponse, redirect
# the index function is called when root is visited
def display(request):
  response = "placeholder to display survey"
  return HttpResponse(response)
def new(request):
  response = "New survey"
  return HttpResponse(response)

