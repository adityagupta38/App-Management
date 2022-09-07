import django
django.setup()
from .models import AdminUser
from django.contrib.auth.models import User
import json

def is_admin_registered(user):
    try:
        user = AdminUser.objects.get(admin_username=user)
        valid = True
    except:
        valid = False
    return valid


def is_authenticated(user, password):

    ''' Here we need to get the model obj 1st and then need to extract req field using field_name of model '''

    admin_obj = AdminUser.objects.get(admin_username=user)
    admin_user = admin_obj.admin_username
    admin_password = admin_obj.password
    if admin_user == user and admin_password == password:
        auth = True
    else:
        auth = False
    return auth


def is_user_registered(username):
    try:
        user = User.objects.get(username=username)
        return True
    except:
        return False


def is_app_added(username, appid):
    try:
        user = User.objects.get(username=username)
        addedapp = user.appsdownloaded.all().get(app_id=appid)
        addedapp_id = addedapp.app_id
        if addedapp_id == appid:
            return True
        else:
            return False
    except:
        return False


