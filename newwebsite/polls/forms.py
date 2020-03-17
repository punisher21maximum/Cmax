from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Owner_model


#extend User model
'''
This is how we extend the inbuit 'User' model, to add more fields.
User (inbuilt model) has only 1]username 2]password1 3]password2
Here adding field --> 4]email
'''
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']



#update User info
'''
Update User info 
(like username or email ; password is not allowed to be changed by using a form)
'''
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

#update Profile info`ty      

'''
Update Profile info
(like dp)'''

class Owner_modelUpdateForm(forms.ModelForm):
    class Meta:
        model = Owner_model
        exclude = ['user']










'''
from django import forms
from django.contrib.auth.models import User

from .models import Book,Seller


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
'''
