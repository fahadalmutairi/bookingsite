from django import forms
from main.models import Property, PropertyImages, Address

class AreaSearchForm(forms.Form):
    area = forms.CharField(required=True)
