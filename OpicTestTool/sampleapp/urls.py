from django.urls import path
from .views import Home, Contact

urlpatterns = [
    path('', Home, name='Home'),
    path('contact/', Contact, name='contact'),
]
