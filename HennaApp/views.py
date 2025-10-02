from django.shortcuts import render

# Create your views here.

def Home(request):
    return render(request,'index.html')

def About(request):
    return render(request,'about_page.html')

def Service(request):
    return render(request,'service_page.html')

def Gallery(request):
    return render(request,'gallery_page.html')