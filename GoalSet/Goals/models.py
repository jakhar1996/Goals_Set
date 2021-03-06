from __future__ import unicode_literals

from django.db import models

# Create your models here.
class goal(models.Model):
	title = models.CharField(max_length = 120)
	#slug = models.SlugField(unique=True)
	#image = models.FileField(null=True, blank=True)
	today = models.TextField()
	tomorrow = models.TextField()
	week = models.TextField()
	date = models.DateTimeField(auto_now = False, auto_now_add = True)
	update = models.DateTimeField(auto_now = True, auto_now_add = False)

	def __unicode__(self):
		return self.title

	def get_absolute_url(self):
		return "/goal/%s/" %(self.id)