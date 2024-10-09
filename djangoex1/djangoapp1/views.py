from django.shortcuts import render
from djangoapp1.models import Patients
from django.http import HttpResponse


def index(request):
    context = {}
    patients = Patients.objects.all()
    context['patients'] = patients
    context['title'] = 'Home'
    return render(request, 'index.html', context)


def about(request):
    context = {}
    context['title'] = 'About'
    return render(request, 'about.html', context)

# Create your views here.
