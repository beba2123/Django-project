from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from.models import  Project
from .forms import ProjectForm
projectsList=[
    {
    'id':'1',
    'title':'Ecommerce website',
    'discription':'Fully functional ecommerce website'
    },
    {
    'id':'2',
    'title':'Portfolio website',
    'discription':'This was a project where i built out my portfolio'
    },
    {
    'id':'3',
    'title':'Social Network',
    'discription':'Awesome open source project i am still working on'
    },
]

def projects(request):
   projects= Project.objects.all()
   context = {'projects':projects}
   return render(request,'projectss/projects.html',context)
def project(request,pk):
    projectobj=Project.objects.get(id=pk)
    print(projectobj)
    return render(request,'projectss/SingleProject.html',{'project':projectobj})

@login_required(login_url="login")
def createProject(request):
    profile = request.user.profile
    form =ProjectForm()

    if request.method == 'POST':
     form = ProjectForm(request.POST, request.FILES)
     if form.is_valid():
        project = form.save(commit=False)
        project.owner = profile
        project.save()
        form.save()
        return redirect('projects')
    context={'form':form}
    return render(request,'projectss/project_form.html',context)

@login_required(login_url="login")
def updateproject(request,pk):
    profile = request.user.profile
    project = profile.project_set.get(id=pk)
    form =ProjectForm(instance=project)
    if request.method == 'POST':
     form = ProjectForm(request.POST,request.FILES, instance=project)
     if form.is_valid():
        form.save()
        return redirect('projects')
    context={'form':form}
    return render(request,'projectss/project_form.html',context)

@login_required(login_url="login")
def  deleteProject(request,pk):
   profile = request.user.profile
   project = profile.project_set.get(id=pk)
   if request.method == 'POST':
      project.delete();
      return redirect('projects')
   context= {'object': project}
   return render(request, 'delete_object.html', context)
