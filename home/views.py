from django.shortcuts import render, get_object_or_404


# Create your views here.
def get_index(request):
    return render(request, 'index.html')
    
def get_about(request):
    return render(request, 'about.html')