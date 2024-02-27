from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Profile 

from .forms import RegisterForm, LoginForm, ProfileForm

def signupuser(request):
    if request.user.is_authenticated:
        return redirect(to='project:main')

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='project:main')
        else:
            return render(request, 'users/signup.html', context={"form": form})

    return render(request, 'users/signup.html', context={"form": RegisterForm()})

def loginuser(request):
    if request.user.is_authenticated:
        return redirect(to='project:main')

    if request.method == 'POST':
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is None:
            messages.error(request, 'Username or password didn\'t match')
            return redirect(to='users:login')

        login(request, user)
        return redirect(to='project:main')

    return render(request, 'users/login.html', context={"form": LoginForm()})

@login_required
def logoutuser(request):
    logout(request)
    return redirect(to='project:main')

@login_required
def profile(request):
    try:
        profile_instance = request.user.profile
    except Profile.DoesNotExist:
        profile_instance = None

    if request.method == 'POST':
        profile_form = ProfileForm(request.POST, request.FILES, instance=profile_instance)
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, 'Your profile is updated successfully')
            return redirect(to='users:profile')

    profile_form = ProfileForm(instance=profile_instance)
    return render(request, 'users/profile.html', {'profile_form': profile_form})
# from django.contrib import messages
# from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.decorators import login_required
# from django.shortcuts import render, redirect

# from .forms import RegisterForm, LoginForm, ProfileForm


# def signupuser(request):
#     if request.user.is_authenticated:
#         return redirect(to='project:main')

#     if request.method == 'POST':
#         form = RegisterForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect(to='project:main')
#         else:
#             return render(request, 'users/signup.html', context={"form": form})

#     return render(request, 'users/signup.html', context={"form": RegisterForm()})


# def loginuser(request):
#     if request.user.is_authenticated:
#         return redirect(to='project:main')

#     if request.method == 'POST':
#         user = authenticate(username=request.POST['username'], password=request.POST['password'])
#         if user is None:
#             messages.error(request, 'Username or password didn\'t match')
#             return redirect(to='users:login')

#         login(request, user)
#         return redirect(to='project:main')

#     return render(request, 'users/login.html', context={"form": LoginForm()})


# @login_required
# def logoutuser(request):
#     logout(request)
#     return redirect(to='project:main')


# @login_required
# def profile(request):
#     if request.method == 'POST':
#         profile_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
#         if profile_form.is_valid():
#             profile_form.save()
#             messages.success(request, 'Your profile is updated successfully')
#             return redirect(to='users:profile')

#     profile_form = ProfileForm(instance=request.user.profile)
#     return render(request, 'users/profile.html', {'profile_form': profile_form})