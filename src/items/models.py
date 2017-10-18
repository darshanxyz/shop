from __future__ import unicode_literals
from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

class Item(models.Model):
	title = models.CharField(max_length=30)
	image = models.FileField(null=True, blank=True)
	description = models.TextField()
	brand = models.CharField(max_length=30, null=True)
	rating = models.FloatField(default=0)
	price = models.IntegerField(default=1000)
	users = models.ManyToManyField(User, related_name='users')
	sum_of_ratings = models.IntegerField(default=0)
	number_of_ratings = models.IntegerField(default=0)
	rated = models.ManyToManyField(User, related_name='users_rated')
	category = models.ForeignKey('Category', on_delete=models.CASCADE, null=True)

	def __unicode__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('items:detail', kwargs = {'id': self.id})

class Category(models.Model):
	title = models.CharField(max_length=50)

	def __unicode__(self):
		return self.title