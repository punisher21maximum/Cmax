# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.

from .models import Book_model,Owner_model,Etx_model,Novel_model,Ebook_model,Enotes_model,Arduino_model,Calc_model

admin.site.register(Owner_model)
admin.site.register(Book_model)
admin.site.register(Etx_model)
admin.site.register(Novel_model)
admin.site.register(Ebook_model)
admin.site.register(Enotes_model)

admin.site.register(Arduino_model)
admin.site.register(Calc_model)