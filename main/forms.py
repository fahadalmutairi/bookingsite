from django import forms
from main.models import Property

class AddPropertyForm(forms.ModelForm):
	class Meta:
		model = Property
		fields = ['name', 'description', 'bedrooms', 'floors', 'rate_by_day',
				'rate_by_week', 'longitude', 'latitude']

class EditPropertyFrom(forms.ModelForm):
	class Meta:
		model = Property
		fields = ['name', 'description', 'bedrooms', 'floors', 'rate_by_day',
				'rate_by_week', 'longitude', 'latitude']		




