from typing import Any
from django import forms
from django.contrib.auth.base_user import AbstractBaseUser
from django.forms import ModelForm,widgets,Widget
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm,UserChangeForm,AuthenticationForm

class makePersonalDetails(forms.Form):
    name=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Enter your name"}))
    email=forms.EmailField(widget=forms.EmailInput(attrs={"class":"form-control","placeholder":"Enter your email"}))
    department=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    dep_code=forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-control"}))
    password=forms.IntegerField(widget=forms.PasswordInput(attrs={"class":"form-control"}))

class loginForms(AuthenticationForm):
    class Meta:
        model=AuthenticationForm
        fields=['username','password']
    def __init__(self,*args: Any, **kwargs: Any):
        super(loginForms,self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class']='form-control'
        self.fields['password'].widget.attrs['class']='form-control'


class createUserusingCreationForm(UserCreationForm):
    class Meta:
        model=User
        #fields="__all__"
        fields=['username','first_name','last_name','email','password1','password2']
        widgets={
            "username":forms.TextInput(attrs={'class':'form-control'}),
            "first_name":forms.TextInput(attrs={'class':'form-control'}),
            "last_name":forms.TextInput(attrs={'class':'form-control'}),
            "email":forms.EmailInput(attrs={'class':'form-control'}),
        }

    def __init__(self, *args, **kwargs):
            super(createUserusingCreationForm,self).__init__(*args,*kwargs)

            self.fields['password1'].widget.attrs['class']='form-control'   
            self.fields['password2'].widget.attrs['class']='form-control'   


class passChangewithOldp(PasswordChangeForm):
    class Meata:
        model=User
        fields=['old_password','new_password1','new_password']

    def __init__(self, *args: Any, **kwargs: Any):
        super(passChangewithOldp,self).__init__( *args, **kwargs)

        self.fields['old_password'].widget.attrs['class']='form-control'
        self.fields['new_password1'].widget.attrs['class']='form-control'
        self.fields['new_password2'].widget.attrs['class']='form-control'

    


# UserChangeForm 
class modifyUser(UserChangeForm):
    password=None
    class Meta:
        model=User
        fields=['username','first_name','last_name','email','is_active','is_staff','is_superuser']
        widgets={
            "username":forms.TextInput(attrs={'class':'form-control'}),
            "first_name":forms.TextInput(attrs={'class':'form-control'}),
            "last_name":forms.TextInput(attrs={'class':'form-control'}),
            "email":forms.EmailInput(attrs={'class':'form-control'}),
        }
        