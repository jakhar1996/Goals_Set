from django.contrib import admin
from .models import goal
# Register your models here.

class goalAdmin(admin.ModelAdmin):
	list_display = ["title", "update", "date"]
	list_filter = ["title", "date"]
	search_fields = ["title", "today"]
	class Meta:
		model = goal
admin.site.register(goal, goalAdmin )