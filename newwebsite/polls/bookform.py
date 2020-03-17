from django import forms
from django.db import models
from django.forms import ModelForm
lenn=100

'''
from .models import Book_model

class fun_book_form(ModelForm):
    class Meta:
        model = Book_model
        fields = '__all__'

'''
'''
class fun_book_form(forms.Form):
	
	seller = forms.CharField()#change to Foreign Key later
	material_name=forms.CharField()
	book_name=forms.CharField()
	book_image=forms.FileField()

	book_branch=forms.CharField()
	book_sub=forms.CharField()
	book_year=forms.CharField()

	author=forms.CharField()
	edition=forms.CharField()
	sell_price=forms.CharField()
	rent_price_per_month=forms.CharField()
	rent_price_per_week=forms.CharField()
'''
