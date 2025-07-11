from django.shortcuts import render

# Home Page.
def home(request):
    return render(request,'home,html')

# Project Page.
def home(request):
    return render(request,'project,html')

# About.
def about(request):
    return render(request,'about,html')

# Contact Page.
def contact(request):
    return render(request,'contact,html')

# Hire Page.
def hire(request):
    return render(request,'hire,html')
