from django.shortcuts import render

# Create your views here.
def projects(request):
    return render(request, 'projects.html')

def project(request):
    return render(request, 'single_project.html')