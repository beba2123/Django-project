from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from.models import  Project , Tag
from .forms import ProjectForm
from  django.db.models import Q
from  .utils import searchProject
from django.core.paginator import Paginator  , PageNotAnInteger  , EmptyPage



def projects(request):
    projects, search_query = searchProject(request)
    
    page= request.GET.get('page')
    result= 3
    paginator = Paginator(projects, result) #this is used for  list 3 projects per all projects.

    try:
        projects= paginator.page(page) #this is used for listing the 3-projects per page.
    except PageNotAnInteger:
        page=1
        projects= paginator.page(page)
    except EmptyPage:
       page = paginator.num_pages  #used for giving the last page in my webite.
       projects = paginator.page(page)
    
    leftIndex = (int(page)-4)

    if leftIndex < 1:
       leftIndex =1;
    
    rightIndex = (int(page)+5);
    if rightIndex > paginator.num_pages:
       rightIndex =paginator.num_pages


    custom_range = range(leftIndex, rightIndex) #for creating  interval  between pagination button numbers..
    context = {'projects':projects ,'search_query': search_query , 
               'paginator': paginator, 'custom_range':custom_range}
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
