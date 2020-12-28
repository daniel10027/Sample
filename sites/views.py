from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView, ListView, UpdateView, View, DetailView


def Home(request):
    
    return render(request, 'sites/index.html')