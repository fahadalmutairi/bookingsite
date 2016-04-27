from django import forms

from main.models import Property, PropertyImages, Address

class AreaSearchForm(forms.Form):
    area = forms.CharField(required=True)


class AddPropertyForm(forms.ModelForm):
	class Meta:
		model = Property
		fields = ['name', 'description', 'bedrooms', 'floors', 'rate_by_day',
				'rate_by_week', 'longitude', 'latitude']

class EditPropertyFrom(forms.ModelForm):
	img = forms.ImageField()
	class Meta:
		model = Property
		fields = ['name', 'description', 'bedrooms', 'floors', 'rate_by_day',
				'rate_by_week', 'longitude', 'latitude']		

class AddImageForm(forms.ModelForm):
	class Meta:
		model = PropertyImages
		fields = '__all__'
