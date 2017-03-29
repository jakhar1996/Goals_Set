from django import forms
from django.contrib.auth import (
	authenticate,
	get_user_model,
	login,
	logout,

	)

users = get_user_model()



class UserLoginForm(forms.Form):
	username = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput)

	def clean(self, *args, **kwargs):
		username = self.cleaned_data.get("username")
		password = self.cleaned_data.get("password")
		user = authenticate(username=username, password=password)
		if not user:
			raise forms.ValidationError('THis user does not exist')
		if not 	user.check_password(password):
			raise forms.ValidationError("password is incorrect")
		if not user.is_active:
			raise forms.ValidationError("this user is not active")
		return super(UserLoginForm, self).clean(*args, **kwargs)

class UserRegisterForm(forms.ModelForm):
	email = forms.EmailField(label="Email")
	email2 = forms.EmailField(label="Confirm Email")
	password = forms.CharField(widget=forms.PasswordInput)

	class Meta:
		model = users
		fields = [
			"username",
			"email",
			"email2",
			"password",
		]

	def clean_email2(self):
		email = self.cleaned_data.get("email")
		email2 = self.cleaned_data.get("email2")
		if email != email2:
			raise forms.ValidationError("Email Must Match")

		email_qs = users.objects.filter(email=email)
		if email_qs.exists():
			raise forms.ValidationError("This email is already registered")

		return email

	'''
	def clean(self, *args, **kwargs):
		email = self.cleaned_data.get("email")
		email2 = self.cleaned_data.get("email2")
		if email != email2:
			raise forms.ValidationError("Email Must Match")

		email_qs = users.objects.filter(email=email)
		if email_qs.exists():
			raise forms.ValidationError("This email is already registered")

		return super(UserRegisterForm, self).clean(*args, **kwargs)
'''