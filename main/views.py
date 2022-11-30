from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Task, UserChallenge, Profile
import datetime

def loginPage(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('main')
        messages.add_message(request, messages.ERROR, 'Username or password is incorrect!')
    return render(request, 'main/login.html')

def registerPage(request):
    form = CustomUserCreationForm()
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            user = authenticate(request, username=user.username, password=request.POST['password1'])
            if user is not None:
                login(request, user)
                messages.add_message(request, messages.SUCCESS, 'Registration successful.')
                return redirect('main')

    context = {'form':form}
    return render(request, 'main/register.html', context=context)

@login_required(login_url='login', redirect_field_name='')
def mainPage(request):
    my_time = datetime.datetime.utcnow()
    day = my_time.day
    month = my_time.strftime("%B")
    weekday = my_time.strftime('%A')

    if request.method == 'POST':
        if request.POST['new-task']:
            task = Task(title=request.POST['new-task'], user=request.user)
            task.save()
            return redirect('main')

    challenges = UserChallenge.objects.filter(participant=request.user)
    tasks = Task.objects.filter(user=request.user)
    context = {'tasks': tasks, 'challenges': challenges, 'day': day, 'month': month, 'weekday': weekday}
    return render(request, 'main/main.html', context)

def friends(request):
    profile = Profile.objects.get(user=request.user)
    context = {'profile': profile}
    return render(request, 'main/friends.html', context)

def logoutPage(request):
    logout(request)
    return redirect('login')
