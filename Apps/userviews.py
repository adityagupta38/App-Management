import django
django.setup()
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from Apps.forms import UserSignupForm, AppsDownloadedForm
from django.contrib import messages
from Apps.mixins import is_user_registered, is_app_added
from Apps.models import Apps
from django.contrib.auth.decorators import login_required
from django.db.models import Sum, Count


def user_signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        if not is_user_registered(username=username):
            userform = UserSignupForm(request.POST)
            if userform.is_valid():
                password = userform.cleaned_data.get('password')
                user = userform.save(commit=False)
                user.set_password(password)
                user.save()
                messages.add_message(request, messages.SUCCESS, 'Signup Successfull Log In To Continue')
                return redirect('userlogin/')
            error = userform.errors
            userform = UserSignupForm()
            return render(request, 'user_registration.html', {'form': userform, 'errors': error})
        error = 'Username is already Registered Pls try different Username'
        userform = UserSignupForm()
        return render(request, 'user_registration.html', {'form': userform, 'msg': error})
    userform = UserSignupForm()
    return render(request, 'user_registration.html', {'form': userform})


@login_required(login_url='/userlogin/')
def user_home(request):
    apps = Apps.objects.all()
    return render(request, 'user_home.html', {'apps': apps})


@login_required(login_url='/userlogin/')
def userprofile(request):
    username = request.user
    user = User.objects.get(username=username)
    return render(request, 'user_profile.html', {'user': user})


@login_required(login_url='/userlogin/')
def user_app_detail(request, pk):
    if request.method == 'POST':
        username = request.user
        if not is_app_added(username, appid=pk):
            appssform = AppsDownloadedForm(files=request.FILES)
            if appssform.is_valid():
                user_obj = User.objects.get(username=username)
                app_obj = Apps.objects.get(id=pk)
                app_point = app_obj.points
                add_app = appssform.save(commit=False)
                add_app.user = user_obj
                add_app.app = app_obj
                add_app.points_earned = app_point
                add_app.save()
                messages.add_message(request, messages.SUCCESS, 'App Screenshot Successfully Addedd')
                return redirect(f'/userappdetail{pk}')
            errors = appssform.errors
            app = Apps.objects.get(id=pk)
            appssform = AppsDownloadedForm()
            return render(request, 'user_app_detail_form.html', {'app': app, 'appss': appssform, 'errors': errors})
        errmsg = 'App Screenshot Is Already Added'
        app = Apps.objects.get(id=pk)
        appssform = AppsDownloadedForm()
        return render(request, 'user_app_detail_form.html', {'app': app, 'appss': appssform, 'errmsg': errmsg})
    app = Apps.objects.get(id=pk)
    appssform = AppsDownloadedForm()
    return render(request, 'user_app_detail_form.html', {'app': app, 'appss': appssform})


@login_required(login_url='/userlogin/')
def userpoints(request):
    username = request.user
    user = User.objects.get(username=username)
    try:
        user_points = user.appsdownloaded.all().aggregate(Sum('points_earned'))
    except:
        user_points = None
    return render(request, 'user_points_earned.html', {'user': user, 'points': user_points})


@login_required(login_url='/userlogin/')
def usertask(request):
    username = request.user
    user = User.objects.get(username=username)
    try:
        task_comp = user.appsdownloaded.all().aggregate(Count('app_id'))
    except:
        task_comp = None
    return render(request, 'user_task_completed.html', {'user': user, 'tasks': task_comp})
