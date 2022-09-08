from django.shortcuts import render, redirect
from Apps.forms import AdminRegForm, AdminLoginForm, AppModForm
from .mixins import is_admin_registered, is_authenticated
from .models import AdminUser, Apps
from django.contrib import messages
import os
from AppManagement.settings import BASE_DIR
# Create your views here.


def admin_login(request):
    form = AdminLoginForm()
    if request.method == 'POST':
        user = request.POST['username']
        password = request.POST['password']
        if not is_admin_registered(user):
            msg = 'Username is Not Registerd Pls Register First'
            return render(request, 'admin_login.html', {'form': form, 'msg': msg})
        if is_authenticated(user, password):
            admin_user = AdminUser.objects.get(admin_username=user)
            admin_id = admin_user.id
            return redirect(f'/adminhome{admin_id}')
        msg = 'Username or password is incorrect'
        return render(request, 'admin_login.html', {'form': form, 'msg': msg})
    return render(request, 'admin_login.html', {'form': form})


def admin_home(request, pk):
    admin_user = AdminUser.objects.get(id=pk)
    apps = Apps.objects.all()
    return render(request, 'admin_home.html', {'user': admin_user, 'apps': apps})


def admin_register(request):
    form = AdminRegForm()
    if request.method == 'POST':
        user = request.POST['admin_username']
        if is_admin_registered(user):
            msg = 'Username Is Already Registerd Pls Try Different Username'
            return render(request, 'admin_registeration_form.html', {'form': form, 'msg': msg})
        form = AdminRegForm(request.POST)
        if form.is_valid():
            form.save()
            msg = f'{user} Sucessfully Registered'
            messages.add_message(request, messages.SUCCESS, msg)
            return redirect('/adminlogin/')
        msg = "Passwords Doesn't Match Pls Check It Again"
        return render(request, 'admin_registeration_form.html', {'form': form, 'msg': msg})
    return render(request, 'admin_registeration_form.html', {'form': form})


def add_app(request, id):
    admin_id = id
    admin_obj = AdminUser.objects.get(id=admin_id)
    if request.method == 'POST':
        '''''
        admin_id = int(request.POST.get('id'))
        admin_obj = AdminUser.objects.get(id=admin_id)
        admin_user = admin_obj.admin_username
        
        form = AddAppForm(request.POST, files=request.FILES)
        if form.is_valid():
            app_image = request.FILES['app_image']
            app_name = request.POST['app_name']
            app_link = request.POST['app_link']
            app_category = request.POST['app_category']
            app_subcategory = request.POST['app_subcategory']
            points = int(request.POST['points'])
            Apps.objects.create(admin_user=admin_obj, app_image=app_image, app_name=app_name, app_link=app_link, app_category=app_category, app_subcategory=app_subcategory, points=points)
            '''''
        form = AppModForm(request.POST, request.FILES)
        if form.is_valid():
            app = form.save(commit=False)  # for updating admin_user field we need to load & save data to cache memory 1st
            app.admin_user = admin_obj
            app.save()
            msg = 'App Added Successfully'
            # here we need to pass admins id for rendering of nav bars add apps field url
            return render(request, 'admin_apps_form.html', {'form': form, 'msg': msg, 'user': admin_obj})
        return render(request, 'admin_apps_form.html', {'form': form, 'msg': form.errors, 'user': admin_obj})
    form = AppModForm()
    return render(request, 'admin_apps_form.html', {'form': form, 'user': admin_obj})


def admin_logout(request):
    return redirect('/adminlogin/')


def home(request):
    return render(request, 'home.html')


def app_delete(request, pk):
    if request.method == "POST":
        user_id = int(request.POST['userid'])
        app = Apps.objects.get(id=pk)
        app_img_path = app.app_image.url
        os.remove('{}{}'.format(BASE_DIR, app_img_path))
        app.delete()
        return redirect(f'/adminhome{user_id}/')
    msg = None
    username = request.GET.get('username')
    user = AdminUser.objects.get(admin_username=username)
    return render(request, 'confirm_app_delete.html', {'user': user, 'msg': msg})
