from django.shortcuts import render
from django.shortcuts import HttpResponse
# Create your views here.


def Home(request):
    return render(request, 'home.html')


def Contact(request):
    return HttpResponse("<h1>This is contact response</h1>")
