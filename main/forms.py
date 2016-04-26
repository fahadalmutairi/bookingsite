from django import forms 
from django.contrib.auth.forms import UserCreationForm , UserChangeForm 
from main.models import CustomUser 

# Create User Form
class CustomUserCreationForm(UserCreationForm):
	def __init__(self, *arg, **kwargs):
		super(CustomUserCreationForm, self).__init__(*arg, **kwargs)
		#del self.fields['username']

	class Meta:
		model = CustomUser
		fields = ("email",)

#Change User Form 
class CustomUserChangeForm(UserChangeForm):
	def __init__(self, *args, **kwargs):
		super(CustomUserChangeForm, self).__init__(*arg, **kwargs)
		del self.fields['username']

	class Meta:
		model = CustomUser
		fields = '__all__'

#User Login Form
class CustomUserLoginForm(forms.Form):
	email = forms.CharField(required=True)
	password = forms.CharField(required=True, widget=forms.PasswordInput())

#Edit Profile Form
class EditProfileForm(forms.ModelForm):
	class Meta:
		model = CustomUser
		fields = ['first_name', 'last_name']
