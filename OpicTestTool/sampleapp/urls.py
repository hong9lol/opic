from django.urls import path
from .views import Sample, Contact

urlpatterns = [
    path('', Sample, name='Sample'),
    path('contact/', Contact, name='contact'),
]
