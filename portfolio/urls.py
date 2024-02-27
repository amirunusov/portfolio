from django.urls import path

from portfolio.views import *

urlpatterns = [
    path('', home, name='home'),
]
