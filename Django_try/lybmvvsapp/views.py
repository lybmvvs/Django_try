from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'lybmvvsapp/index.html')

def about(request):
    return render(request, 'lybmvvsapp/about.html')
# Create your views here.
