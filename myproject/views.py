from django.http import HttpResponse
from django.shortcuts import render

def register(request):
    return render(request,'Register.html')
def index(request):
    return render(request,'index.html')