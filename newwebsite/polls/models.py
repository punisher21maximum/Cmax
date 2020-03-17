# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django import forms
# Create your models here.
from django.db import models
from django.utils import timezone
import datetime
#define common max_length for all
lenn=100
#
from django.core.urlresolvers import reverse


#User model
from django.contrib.auth.models import User
#Profile model

#A common 'owner' class for all the 5 classes -- Book,Novel,Etx,Ebook,Enotes
class Owner_model(models.Model):

	user = models.OneToOneField(User,on_delete=models.CASCADE)
	ph_num=models.CharField("phone number",max_length=lenn,null=True)
	ac_year=models.CharField("academic year",max_length=lenn,null=True)
	branch=models.CharField("branch",max_length=lenn,null=True)
	address=models.CharField(max_length=lenn,null=True)
	dp=models.FileField(upload_to='media/owner/pdf',blank=True)
	
	def  get_absolute_url(self):
		return reverse('polls:detail', kwargs={'pk':self.pk})
	def get_fields(self):
		return [(field.name, field.value_to_string(self)) for field in Owner_model._meta.fields]
	

	def __str__(self):
        	return self.user.username

	
#1]Book
class Book_model(models.Model):
	
	owner = models.ForeignKey(User, on_delete=models.CASCADE)
	book_name=models.CharField(max_length=lenn)
	book_image=models.FileField(blank=True,default='book/pdf/no_image.jpg')
	pdf = models.FileField(upload_to='book/pdf',blank=True)
	#star field
	star = models.BooleanField(default = False,blank=True)

	Branch_CHOICES=[('CS','CS'),('Mech','Mech'),('ENTC','ENTC'),('IT','IT'),('CHEM','CHEM'),('ETX','ETX'),('Civil','Civil'),('FY','FY')]
	book_branch=models.CharField(max_length=lenn,choices=Branch_CHOICES,default='CS')

	Subject_CHOICES=[('NO SUBJECT','NO SUBJECT'),('DSF','Data Structures And Files'),
	('DSGT','Data Structures and Graph Theory'),('AM2','Applied Mathematcs'),
	('AM1','Applied Mechanics'),('EI','Engineering Informatics'),('DBMS','DBMS'),('SYSTEM ENGG','SYSTEM ENGG'),
	('MATHS','MATHS'),('PSYCHO','PSYCHO'),('MATERIAL ENGG','MATERIAL ENGG'),('PYTHON','PYTHON'),('CPP','CPP'),
	('EEE','EEE'),
	('None','none')]
	book_sub=models.CharField(max_length=lenn,choices=Subject_CHOICES,default='NO SUBJECT')

	Year_CHOICES=[('I','I'),('II','II'),('III','III'),('IV','IV')]
	book_year=models.CharField(max_length=lenn,choices=Year_CHOICES,default='I')

	author=models.CharField(max_length=lenn)

	import datetime
	YEAR_CHOICES = [(r,r) for r in range(1984, datetime.date.today().year+1)]

	edition = models.IntegerField( ('year'), choices=YEAR_CHOICES, default=datetime.datetime.now().year )

	#edition=models.IntegerField()


	sell_price=models.CharField(max_length=lenn)
	rent_price_per_day=models.CharField(max_length=lenn,null=True,default=20)
	rent_price_per_week=models.CharField(max_length=lenn,null=True,default=50)
	rent_price_per_month=models.CharField(max_length=lenn,null=True,default=100)
	
	def  get_absolute_url(self):
		return reverse('polls:index')

	#star_begin
	def get_add_to_fav_url(self):
	    return reverse("polls:favv", kwargs={ 'pk': self.pk })
	def get_remove_from_fav_url(self):
		return reverse("polls:unfavv", kwargs={ 'pk': self.pk })
	#star_end
	
	def __str__(self):
        	return self.book_name

	def get_fields(self):
		return [(field.name, field.value_to_string(self)) for field in Book_model._meta.fields]

	class Meta:
        	ordering = ('sell_price',)



#3]Novel
class Novel_model(models.Model):
	
	owner = models.ForeignKey(User, on_delete=models.CASCADE)
	novel_name=models.CharField(max_length=lenn)
	novel_image=models.FileField(upload_to='novel/img',default='book/pdf/no_image.jpg',blank=True)

	Genre_CHOICES=[('action','action'),('fiction','fiction'),('romance','romance'),('comedy','comedy'),('biography','biography'),
	('tragedy','tragedy'),('thriller','thriller'),('classic','classic'),('mystery','mystery'),('children','children'),('None','None')]
	genre=models.CharField(max_length=lenn,choices=Genre_CHOICES,null=True,default='classic')

	author=models.CharField(max_length=lenn,null=True)

	import datetime
	Edition_CHOICES = [(r,r) for r in range(1984, datetime.date.today().year+1)]
	edition=models.IntegerField(('year'), choices=Edition_CHOICES, default=datetime.datetime.now().year ,null=True)

	novel_desc=models.CharField(max_length=lenn,null=True)

	pages=models.CharField(max_length=lenn,null=True)
	sell_price=models.CharField(max_length=lenn,null=True,default='300')
	rent_price_per_day=models.CharField(max_length=lenn,null=True,default='25')
	rent_price_per_week=models.CharField(max_length=lenn,null=True,default='50')
	rent_price_per_month=models.CharField(max_length=lenn,null=True,default='150')
	
	def __str__(self):
        	return self.novel_name
	def  get_absolute_url(self):
		return reverse('polls:novel_index')    	
	def get_fields(self):
		return [(field.name, field.value_to_string(self)) for field in Novel_model._meta.fields]
	class Meta:
        	ordering = ('sell_price',)
#4]Enotes
class Enotes_model(models.Model):
	
	owner = models.ForeignKey(User, on_delete=models.CASCADE)
	
	enotes_author=models.CharField(max_length=lenn,)	
	enotes_topic=models.CharField(max_length=lenn, blank=True)
	enotes_desc=models.CharField(max_length=lenn, blank=True)
	enotes_unit=models.PositiveIntegerField(blank=True, default=1)

	from django.contrib.admin.widgets import AdminDateWidget
	from django.forms.fields import DateField
	enotes_date=models.DateField( ("Date"), auto_now_add=True)
 
	enotes_image=models.FileField(upload_to='enotes/img',default='book/pdf/no_image.jpg',blank=True)
	enotes_pdf = models.FileField(upload_to='enotes/pdf',blank=True)
	enotes_drive_url=models.URLField(max_length=lenn,default='http://localhost:8000/polls/',null=True)
	#bsy
	Branch_CHOICES=[('CS','CS'),('Mech','Mech'),('ENTC','ENTC'),('IT','IT'),('CHEM','CHEM'),('ETX','ETX'),('Civil','Civil'),('FY','FY')]

	Subject_CHOICES=[('NO SUBJECT','NO SUBJECT'),('DSF','Data Structures And Files'),
	('DSGT','Data Structures and Graph Theory'),('AM2','Applied Mathematcs'),
	('AM1','Applied Mechanics'),('EI','Engineering Informatics'),('DBMS','DBMS'),('SYSTEM ENGG','SYSTEM ENGG'),
	('MATHS','MATHS'),('PSYCHO','PSYCHO'),('MATERIAL ENGG','MATERIAL ENGG'),('PYTHON','PYTHON'),('CPP','CPP'),
	('EEE','EEE'),
	('None','none')]
	Year_CHOICES=[('I','I'),('II','II'),('III','III'),('IV','IV')]

	enotes_branch=models.CharField(max_length=lenn,choices=Branch_CHOICES,default='CS')
	enotes_sub=models.CharField(max_length=lenn,choices=Subject_CHOICES,default='NO SUBJECT')
	enotes_year=models.CharField(max_length=lenn,choices=Year_CHOICES,default='I')
	#bsy
	
	
	def __str__(self):
        	return self.enotes_topic
	def  get_absolute_url(self):
		return reverse('polls:enotes_index')
	def get_fields(self):
		return [(field.name, field.value_to_string(self)) for field in Enotes_model._meta.fields]
	#class Meta:
        	#ordering = ('sell_price',)
#5]Ebook
class Ebook_model(models.Model):
	
	owner = models.ForeignKey(User, on_delete=models.CASCADE)
	ebook_name=models.CharField(max_length=lenn,blank=True)
	ebook_image=models.FileField(upload_to='ebook/img',default='book/pdf/no_image.jpg',blank=True)
	ebook_pdf = models.FileField(upload_to='ebook/pdf',blank=True)
	ebook_author=models.CharField(max_length=lenn)

	Branch_CHOICES=[('CS','CS'),('Mech','Mech'),('ENTC','ENTC'),('IT','IT'),('CHEM','CHEM'),('ETX','ETX'),('Civil','Civil'),('FY','FY')]

	Subject_CHOICES=[('DS','Data Structures'),('DSGT','Data Structures and Graph Theory'),('AM2','Applied Mathematcs'),('AM1','Applied Mechanics'),('EI','Engineering Informatics')]

	Year_CHOICES=[('I','I'),('II','II'),('III','III'),('IV','IV')]
	
	ebook_branch=models.CharField(max_length=lenn,choices=Branch_CHOICES,default='CS')
	ebook_sub=models.CharField(max_length=lenn,choices=Subject_CHOICES,default='DS')
	ebook_year=models.CharField(max_length=lenn,choices=Year_CHOICES,default='I')


	import datetime
	Edition_CHOICES = [(r,r) for r in range(1984, datetime.date.today().year+1)]
	ebook_edition=models.IntegerField(('year'), choices=Edition_CHOICES, default=datetime.datetime.now().year ,null=True)
	
	
	ebook_drive_url=models.URLField(max_length=lenn,
		default='http://localhost:8000/polls/',
		null=True)


	def __str__(self):
        	return self.ebook_name
	def  get_absolute_url(self):
		return reverse('polls:ebook_index')
	def get_fields(self):
		return [(field.name, field.value_to_string(self)) for field in Ebook_model._meta.fields]
	#class Meta:
        	#ordering = ('sell_price',)


#2]Etx
class Etx_model(models.Model):
	
	owner = models.ForeignKey(User, on_delete=models.CASCADE)
	#optional detail
	item_image=models.FileField(blank=True,default='book/pdf/no_image.jpg' )
	item_image2=models.FileField(blank=True,default='book/pdf/no_image.jpg' )
	item_image3=models.FileField(blank=True,default='book/pdf/no_image.jpg' )

	#required detail
	sell_price=models.CharField(max_length=lenn,null=True)
	rent_price_per_day=models.CharField(max_length=lenn,null=True,default='15')
	rent_price_per_week=models.CharField(max_length=lenn,null=True,default='100')
	rent_price_per_month=models.CharField(max_length=lenn,null=True,default='250')
	
	def __str__(self):
        	return self.sell_price
	def get_fields(self):
		return [(field.name, field.value_to_string(self)) for field in Etx_model._meta.fields]
	def  get_absolute_url(self):
		return reverse('polls:etx_index')
	class Meta:
        	ordering = ('sell_price',)
	
#1]Arduino_model
class Arduino_model(Etx_model):

	Type_CHOICES=[('mega','mega'), ('uno','uno'), ('nano','nano'), ('mini','mini')]
	type_A=models.CharField(max_length=lenn,choices=Type_CHOICES, default='uno') 

	cable=models.BooleanField(default=True)

	Jumper_wires_CHOICES=[('m2m','m2m'), ('m2f','m2f'), ('f2f','f2f'),('none','none')]
	jumper_wires=models.CharField(max_length=lenn,choices=Jumper_wires_CHOICES, default='none') 

	jumper_qty=models.IntegerField(default=0)



	def __str__(self):
        	return self.item_name
	def get_fields(self):
		return [(field.name, field.value_to_string(self)) for field in Arduino_model._meta.fields]
	def  get_absolute_url(self):
		return reverse('polls:etx_index')
	class Meta:
        	ordering = ('sell_price',)
#2]calc
class Calc_model(Etx_model):

	Type_CHOICES=[('Casio FX-991MS','Casio FX-991MS'), ('Casio FX-991ES','Casio FX-991ES'), 
	('other','other')]
	type_A=models.CharField(max_length=lenn,choices=Type_CHOICES, default='Casio FX-991MS') 

	desc=models.CharField(max_length=lenn, default='anything else you wanna tell about calc')

	def __str__(self):
        	return self.item_name
	def get_fields(self):
		return [(field.name, field.value_to_string(self)) for field in Calc_model._meta.fields]
	def  get_absolute_url(self):
		return reverse('polls:etx_index')
	class Meta:
        	ordering = ('sell_price',)	

'''

#2]Etx
class Etx_model(models.Model):
	
	owner = models.ForeignKey(User, on_delete=models.CASCADE)
	#optional detail
	item_image=models.FileField(blank=True,default='book/pdf/no_image.jpg' )
	#required detail
	item_keyword1=models.CharField(max_length=lenn,null=True)
	item_keyword2=models.CharField(max_length=lenn,null=True,default='optional')
	item_keyword3=models.CharField(max_length=lenn,null=True,default='optional')
	item_keyword4=models.CharField(max_length=lenn,null=True,default='optional')
	#optional detail  
	manufacturer=models.CharField(max_length=lenn,null=True,default='optional')
	version=models.CharField(max_length=lenn,null=True,default='optional')
	#required detail
	sell_price=models.CharField(max_length=lenn,null=True)
	rent_price_per_day=models.CharField(max_length=lenn,null=True,default='15')
	rent_price_per_week=models.CharField(max_length=lenn,null=True,default='100')
	rent_price_per_month=models.CharField(max_length=lenn,null=True,default='250')
	
	def __str__(self):
        	return self.item_name
	def get_fields(self):
		return [(field.name, field.value_to_string(self)) for field in Etx_model._meta.fields]
	def  get_absolute_url(self):
		return reverse('polls:etx_index')
	class Meta:
        	ordering = ('sell_price',)
'''

