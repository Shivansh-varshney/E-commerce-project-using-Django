from .models import User
from django import forms
from .models import CustomerAddress
from phonenumber_field.formfields import PhoneNumberField
from django.contrib.auth.forms import (UserCreationForm, AuthenticationForm,
                                       UserChangeForm, PasswordChangeForm)


class customerAddress(forms.ModelForm):
    class Meta:
        model = CustomerAddress
        exclude = ['user', 'status']

        labels = {
            'status': 'Default'
        }

        widgets = {
            'addressname': forms.TextInput(attrs={
                "class": "form-control mt-3",
                'placeholder': ''
            }),
            'housenumber': forms.TextInput(attrs={
                "class": "form-control mt-3",
                'placeholder': ''
            }),
            'landmark': forms.TextInput(attrs={
                "class": "form-control mt-3",
                'placeholder': ''
            }),
            'street': forms.TextInput(attrs={
                "class": "form-control mt-3",
                'placeholder': ''
            }),
            'city': forms.TextInput(attrs={
                "class": "form-control mt-3",
                'placeholder': ''
            }),
            'district': forms.TextInput(attrs={
                "class": "form-control mt-3",
                'placeholder': ''
            }),
            'city': forms.TextInput(attrs={
                "class": "form-control mt-3",
                'placeholder': ''
            }),
            'state': forms.TextInput(attrs={
                "class": "form-control mt-3",
                'placeholder': ''
            }),
            'country': forms.TextInput(attrs={
                "class": "form-control mt-3",
                'placeholder': ''
            }),
            'zipcode': forms.TextInput(attrs={
                "class": "form-control mt-3",
                'placeholder': ''
            }),
        }


class signupForm(UserCreationForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={
        "class": "form-control mt-3",
        "placeholder": "Password"
    }))
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={
        "class": "form-control mt-3",
        "placeholder": "Confirm Password"
    }))
    phone = PhoneNumberField(widget=forms.TextInput(attrs={
        'required': True,
        'class': 'form-control',
        'placeholder': 'Phone Number'
    }))

    class Meta:
        model = User
        fields = ['username', 'email', 'phone', 'first_name', 'last_name']
        labels = {
            'email': 'Email',
        }

        widgets = {
            "username": forms.TextInput(attrs={
                "class": "form-control mt-3",
                'required': True,
                'placeholder': 'Username'
            }),
            "email": forms.EmailInput(attrs={
                "class": "form-control mt-3",
                'placeholder': 'Email Address'
            }),
            "first_name": forms.TextInput(attrs={
                "class": "form-control mt-3",
                'required': True,
                'placeholder': 'First Name'
            }),
            "last_name": forms.TextInput(attrs={
                "class": "form-control mt-3",
                'required': True,
                'placeholder': 'Last Name'
            }),
        }


class loginForm(AuthenticationForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        "class": "form-control mt-3",
        "placeholder": "Password"
    }))
    username = forms.EmailField(widget=forms.TextInput(attrs={
        "class": "form-control mt-3",
        "placeholder": "Email"
    }))


class updateUserForm(UserChangeForm):
    phone = PhoneNumberField(widget=forms.TextInput(attrs={
        'required': True,
        'class': 'form-control',
        'placeholder': 'Phone Number'
    }))

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'phone', 'email']
        labels = {
            'email': 'Email'
        }
        widgets = {
            'username': forms.TextInput(attrs={
                'required': True,
                'class': 'form-control',
                'placeholder': 'Username'
            }),
            'first_name': forms.TextInput(attrs={
                'required': True,
                'class': 'form-control',
                'placeholder': 'First Name'
            }),
            'last_name': forms.TextInput(attrs={
                'required': True,
                'class': 'form-control',
                'placeholder': 'Last Name'
            }),
            'email': forms.EmailInput(attrs={
                'required': True,
                'class': 'form-control',
                'placeholder': 'Email'
            }),
        }

    def __init__(self, *args, **kwargs):
        super(updateUserForm, self).__init__(*args, **kwargs)
        self.fields.pop('password', None)


class updatePasswordForm(PasswordChangeForm):
    old_password = forms.CharField(
        label='Old password', strip=False, widget=forms.PasswordInput(attrs={
            'autofocus': True,
            'class': 'form-control',
            'placeholder': 'Old Password'
        }))
    new_password1 = forms.CharField(
        label='New password', strip=False, widget=forms.PasswordInput(attrs={
            'autofocus': True,
            'class': 'form-control',
            'placeholder': 'New Password'
        }))
    new_password2 = forms.CharField(
        label='Confirm New password', strip=False, widget=forms.PasswordInput(attrs={
            'autofocus': True,
            'class': 'form-control',
            'placeholder': 'Confirm Password'
        }))
