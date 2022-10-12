from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("падение метеорита в ")

def test(request):
    return HttpResponse("<h1>главного кота прательской области отравили.читать подробности.</h1>")