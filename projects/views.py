from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib import messages
from.models import  Project , Tag
from .forms import ProjectForm, ReviewForm
from  django.db.models import Q
from  .utils import searchProject , paginateProject
from django.core.paginator import Paginator  , PageNotAnInteger  , EmptyPage



def projects(request):
    projects, search_query = searchProject(request)
    custom_range, projects = paginateProject(request, projects, 6)
    context = {'projects':projects ,'search_query': search_query , 
               'custom_range':custom_range}
    return render(request,'projectss/projects.html',context)
def project(request,pk):
    projectobj=Project.objects.get(id=pk)
    form = ReviewForm()
    if request.method == 'POST':
       form = ReviewForm(request.POST)
       review = form.save(commit=False)
       review.Project = projectobj
       review.owner = request.user.profile
       review.save()
       messages.success(request, 'Your review was successfully submitted')
       
    return render(request,'projectss/SingleProject.html',{'project':projectobj, 'form': form})

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
