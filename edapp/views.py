from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse

def index(request):
    return HttpResponseRedirect(reverse("home"))

def home(request):
    return render(request, "edapp/home.html")

def help(request):
    return render(request, "edapp/help.html")

def solutions(request):
    return render(request, "edapp/solutions.html")

def problem(request):
    return render(request, "edapp/problem.html")

def sources(request):
    return render(request, "edapp/sources.html")