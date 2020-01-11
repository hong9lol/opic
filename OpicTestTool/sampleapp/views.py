from django.shortcuts import render
from django.shortcuts import HttpResponse
# Create your views here.


def Sample(request):
    return HttpResponse("<h1>This is sample response</h1>")


def Contact(request):
    return HttpResponse("<h1>This is contact response</h1>")
