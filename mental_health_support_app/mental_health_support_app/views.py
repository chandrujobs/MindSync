from django.shortcuts import render
from .models import MentalHealthResource

def index(request):
    return render(request, 'index.html')

def resources(request):
    return render(request, 'resources.html')

def home(request):
    return render(request, 'home.html')

def resources(request):
    resources = MentalHealthResource.objects.all()
    return render(request, 'resources.html', {'resources': resources})

def chat(request):
    return render(request, 'chat.html')
