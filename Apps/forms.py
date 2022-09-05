import django
django.setup()
from django import forms
from .models import AdminUser, Apps, AppsDownloaded
from django.contrib.auth.models import User


class AdminRegForm(forms.ModelForm):
    class Meta:
        model = AdminUser
        fields = '__all__'
        widgets = {'re_password': forms.PasswordInput}

    def clean(self):
        p1 = self.cleaned_data.get('password')
        p2 = self.cleaned_data.get('re_password')
        if p1 != p2:
            raise forms.ValidationError("Passwords Doesn't Match")


class AdminLoginForm(forms.Form):
    username = forms.CharField(max_length=30, widget=forms.TextInput)
    password = forms.CharField(max_length=20, widget=forms.PasswordInput)


class AddAppForm(forms.Form):
    admin_user = forms.CharField(max_length=255, required=False, widget=forms.HiddenInput)
    app_image = forms.ImageField()
    app_name = forms.CharField(max_length=100)
    app_link = forms.URLField(max_length=300)
    app_category_choices = (
        ('Entertainment', 'Entertainment'),
        ('Games', 'Games'),
        ('Finance', 'Finance'),
        ('Health', 'Health & Wellness'),
    )
    app_category = forms.ChoiceField(choices=app_category_choices)
    app_subcategory_choices = (
        ('Social Media', 'Socical Media'),
        ('OTT', 'OTT'),
        ('Action', 'Action'),
        ('Adventure', 'Adventure'),
        ('Acrade', 'Acrade'),
        ('UPI', 'UPI'),
        ('Investments', 'Investments'),
        ('Fitness Tracking', 'Fitness Tracking'),
    )
    app_subcategory = forms.ChoiceField(choices=app_subcategory_choices)
    points = forms.IntegerField(min_value=50)


class AppModForm(forms.ModelForm):
    class Meta:
        model = Apps
        fields = '__all__'
        widgets = {'admin_user': forms.HiddenInput,
                   'app_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'App Name'}),
                   'app_link': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'App Link'}),
                   'points': forms.NumberInput(attrs={'placeholder': 'Add'}),
                   }


class UserSignupForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'first_name', 'last_name']
    password2 = forms.CharField(max_length=255)
    first_name = forms.CharField(max_length=155, required=True)
    last_name = forms.CharField(max_length=155, required=True)

    def clean(self):
        p1 = self.cleaned_data.get('password')
        p2 = self.cleaned_data.get('password2')
        if p1 != p2:
            raise forms.ValidationError("Password Doesn't Match")


class AppsDownloadedForm(forms.ModelForm):
    class Meta:
        model = AppsDownloaded
        fields = '__all__'
