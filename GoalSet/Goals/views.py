from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import goal
from .forms import goal_form
from django.contrib import messages

# Create your views here.
def goal_create(request):
	form = goal_form(request.POST or None, request.FILES or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		messages.success(request, "Successfully Created")
		return HttpResponseRedirect(instance.get_absolute_url())
	context = {
		"form" : form,
	}
	return render (request, "post_create.html", context)


def goal_detail(request, id=None):
	instance = get_object_or_404(goal, id=id)
	context = {
		"instance" : instance,
		"title" : instance.title
	}
	return render (request, "post_detail.html", context)

def goal_list(request):
	queryset = goal.objects.all().order_by("-date")
	context = {
		"queryset" : queryset,
		"title" : "Goals"
	}
	return render (request, "post_list.html", context)


def goal_update(request, id=None):
	instance = get_object_or_404(goal, id=id)
	form = goal_form(request.POST or None,request.FILES or None, instance=instance)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		messages.success(request, "Saved")
		return HttpResponseRedirect(instance.get_absolute_url())
	context = {
		"instance" : instance,
		"title" : instance.title,
		"form" : form,
	}
	return render (request, "post_create.html", context)


def goal_delete(request, id=None):
	instance = get_object_or_404(goal, id=id)
	instance.delete()
	messages.success(request, "Deleted")
	return redirect("list")







