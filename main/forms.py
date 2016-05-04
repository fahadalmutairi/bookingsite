from django import forms
from django.contrib.auth.forms import UserCreationForm , UserChangeForm 
from main.models import Property, PropertyImages, Address, Schedule, Booking,CustomUser, Booking
import datetime
from django.forms.extras.widgets import SelectDateWidget

class FilterTime(forms.Form):
	start = forms.DateField(widget=SelectDateWidget)
	end = forms.DateField(widget=SelectDateWidget)

# Create User Form
class AreaSearchForm(forms.Form):
    area = forms.CharField(required=True)

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


class OwnerAddScheduleForm(forms.ModelForm):
	class Meta:
		model = Schedule
		fields = ['date_start','date_end']
		widgets = {'date_start':SelectDateWidget(), 'date_end':SelectDateWidget()}

class UserBookForm(forms.ModelForm):
	class Meta:
		model = Booking
		fields = '__all__'



class AddPropertyForm(forms.ModelForm):
	img = forms.ImageField()
	class Meta:
		model = Property
		fields = ['name', 'description', 'bedrooms', 'floors', 'rate_by_day',
				'rate_by_week', 'longitude', 'latitude']

class EditPropertyFrom(forms.ModelForm):
	class Meta:
		model = Property
		fields = ['name', 'description', 'bedrooms', 'floors', 'rate_by_day',
				'rate_by_week', 'longitude', 'latitude']		

class AddImageForm(forms.ModelForm):
	class Meta:
		model = PropertyImages
		fields = '__all__'

class CheckForm(forms.Form):
	From_date = forms.DateField(widget=SelectDateWidget)
	To_date = forms.DateField(widget=SelectDateWidget)



class BookingForm(forms.ModelForm):
	class Meta:
		model = Booking
		fields = '__all__'

