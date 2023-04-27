from django.shortcuts import redirect, render
from . models import Profile
from django.contrib.auth.models import User
from django.contrib.auth import login,  authenticate , logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import coustomUserCreationForm, ProfileForm, SkillForm
# Create your views here.
def userlogin(request):
    if request.user.is_authenticated:
        return redirect('profiles')

    if request.method == 'POST' :
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'Username does not exists')
        
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('profiles')
        else:
           messages.error(request, 'Username or password  is incorrect..')
           
    return render(request, 'users/login_register.html')

def userlogout(request):
    logout(request)
    messages.info(request, 'User  was logged out!')
    return redirect('login')

def registeruser(request):
    page = 'register'
    form = coustomUserCreationForm()
    if request.method == 'POST':
        form = coustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request, 'User acount is created..!!')
            
            login(request, user)
            return redirect('edit-account')
        else:
            messages.success(request, 'User acount isnot created...!')

    context = {'page': page, 'form':form}
    return render(request, 'users/login_register.html', context)

def profiles(request):
    profiles = Profile.objects.all()
    context = {'profiles': profiles}
    return render(request, 'users/profiles.html', context)

def userProfile(request, pk):
    profile = Profile.objects.get(id=pk)
    topskills = profile.skill_set.exclude(discription__exact="")
    otherskills = profile.skill_set.filter(discription="")
    context = {'profile':profile, 'topskills':topskills, 'otherskills':otherskills}
    return render(request, 'users/user-profile.html', context)
@login_required(login_url='login')
def userAccount(request):
    profile = request.user.profile
    skills = profile.skill_set.all()
    projects = profile.project_set.all()
   
    context={'profile':profile, 'skills':skills, 'projects': projects}
    return render(request, 'users/account.html', context)


@login_required(login_url='login')
def editAccount(request):
    profile = request.user.profile
    form = ProfileForm(instance=profile)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()

            return redirect('account')
    context ={'form': form}
    return render(request, 'users/profile_form.html',context)

@login_required(login_url='login')
def createSkill(request):
    profile = request.user.profile
    form = SkillForm()
    if request.method == 'POST':
        form = SkillForm(request.POST)
        if form.is_valid():
            skill = form.save(commit=False)
            skill.owner = profile
            skill.save()
            return redirect('account')

    context = {'form': form}
    return render(request, 'users/skill_form.html', context)