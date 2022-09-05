

from django.db import models
from django.contrib.auth.models import User



# Create your models here.

# Creating Model to Register Admin Users


class AdminUser(models.Model):
    admin_username = models.CharField(max_length=30, unique=True)
    name = models.CharField(max_length=150)
    password = models.CharField(max_length=20)
    re_password = models.CharField(max_length=20)
    class Meta:
        db_table = 'AdminUser'



class Apps(models.Model):
    admin_user = models.ForeignKey(AdminUser, on_delete=models.CASCADE, null=True, editable=False, default=None)
    app_image = models.ImageField(upload_to='app_icons/')
    app_name = models.CharField(max_length=100, unique=True)
    app_link = models.URLField(max_length=300, unique=True)
    app_category_choices = (
        ('', 'App Category'),
        ('E-Commerce', 'E-Commerce'),
        ('Entertainment', 'Entertainment'),
        ('Games', 'Games'),
        ('Finance', 'Finance'),
        ('Health', 'Health & Wellness'),
        ('Jobs & Business', 'Jobs & Business'),
        ('Education', 'Education'),
                            )
    app_category = models.CharField(max_length=255, choices=app_category_choices)
    app_subcategory_choices = (
        ('', 'App Subcategory'),
        ('Shopping', 'Shopping'),
        ('Social Media', 'Socical Media'),
        ('Networking', 'Networking'),
        ('OTT', 'OTT'),
        ('Action', 'Action'),
        ('Adventure', 'Adventure'),
        ('Acrade', 'Acrade'),
        ('Role Playing', 'Role Playing'),
        ('UPI', 'UPI'),
        ('Investments', 'Investments'),
        ('Fitness Tracking', 'Fitness Tracking'),
    )
    app_subcategory = models.CharField(max_length=255, choices=app_subcategory_choices)
    points = models.PositiveIntegerField()


class AppsDownloaded(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='appsdownloaded', editable=False)
    app = models.ForeignKey(Apps, on_delete=models.CASCADE, related_name='appsdownloaded', editable=False)
    app_ss = models.ImageField(upload_to='app screenshots')
    points_earned = models.PositiveIntegerField(editable=False)
