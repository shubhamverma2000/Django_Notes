from django.shortcuts import render

# Create your views here.
def projects(request):
    return render(request, 'first_app/projects.html')

def project(request):
    return render(request, 'first_app/single_project.html')
