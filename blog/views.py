from django.shortcuts import render

def home(request):
    return render(request, 'blog/home.html', {})

def platform(request):
    return render(request, 'blog/platform.html', {})

def customer(request):
    return render(request, 'blog/customer.html', {})

def team(request):
    return render(request, 'blog/team.html', {})

def contact(request):
    return render(request, 'blog/contact.html', {})

    