from django.shortcuts import render

databaselist=[
    {
        'name':'Shubham Verma',
        'id' : '1',
        'isStudent': True
    },
    {
        'name':'Suyash Pathak',
        'id' : '2',
        'isStudent': False
    }
]

# Create your views here.
def projects(request, pk):
    projectObject = None
    for i in databaselist:
        if i['id']==str(pk):
            projectObject= i
    return render(request, 'first_app/projects.html', {'projectObject':projectObject }) 

def project(request):
    age=21
    name='Shubham Verma'
    context={'age':age, 'name':name, 'projects':databaselist}
    return render(request, 'first_app/single_project.html', context)
