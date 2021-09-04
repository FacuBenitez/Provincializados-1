from django.http import HttpResponse
from django.template import Template, Context
from django.shortcuts import render

def triviaPlantilla(request):
     return render(request, 'home.html')