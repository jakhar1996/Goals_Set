from django import forms
from .models import goal

class goal_form(forms.ModelForm):
	class Meta():
		model = goal
		fields = [
			"title",
			#"image",
			"today",
			"tomorrow",
			"week"
		]