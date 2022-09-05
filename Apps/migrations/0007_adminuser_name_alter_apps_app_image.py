# Generated by Django 4.0.4 on 2022-09-05 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Apps', '0006_alter_apps_admin_user_alter_apps_app_category_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='adminuser',
            name='name',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='apps',
            name='app_image',
            field=models.ImageField(upload_to='app_icons/'),
        ),
    ]
