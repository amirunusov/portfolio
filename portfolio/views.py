from django.shortcuts import render
from django.views.generic import ListView

from portfolio.models import Contact


def home(request):
    print(request.method)
    if request.method == 'POST':
        print(request.POST)
        name = request.POST.get('name')
        print(name)
        email = request.POST.get('email')
        print(email)
        description = request.POST.get('description')
        contact = Contact(name=name, description=description, email=email)
        contact.save()
    return render(request, 'index.html')


def contact_view(request):
    print(2222222)
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        description = request.POST.get('description')
        contact = Contact(name=name, description=description, email=email)
        contact.save()
    return render(request, 'index.html')


