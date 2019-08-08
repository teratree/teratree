from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

def home(request):
    context = {}
    return render(request, 'experiment/home.html', context)

