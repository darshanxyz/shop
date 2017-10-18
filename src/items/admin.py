# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Item, Category

class ItemModelAdmin(admin.ModelAdmin):
	list_display = ['title', 'rating', 'price', 'category']
	search_fields = ['title', 'rating', 'category']
	class Meta:
		model = Item

class CategoryModelAdmin(admin.ModelAdmin):
	list_display = ['title']
	search_fields = ['title']
	class Meta:
		model = Category

admin.site.register(Item, ItemModelAdmin)
admin.site.register(Category, CategoryModelAdmin)