from django.urls import path
from .views import *

urlpatterns = [
    path('', main, {'template_name': 'index.html'}),
]
