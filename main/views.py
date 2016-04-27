from django.shortcuts import render, redirect, render_to_response,get_object_or_404
from main.models import Property
from main.forms import AddPropertyForm, EditPropertyFrom
# Create your views here.

def add_property(request):
	context = {}
	context['form'] = AddPropertyForm()
	if request.method == 'POST':
		form = AddPropertyForm(request.POST, request.FILES)

		if form.is_valid():
			property_object = form.save(commit=False)
			property_object.owner = request.user
			property_object.save()
			return redirect('/profile/')
	return render(request, 'add_property.html', context)

def edit_property(request, pk):
	context = {}
	property_object = Property.objects.get(pk=pk)
	if property_object.owner != request.user:
		return redirect('/propertylist/')
	form = EditPropertyFrom (request.POST or None, instance=property_object)
	context['form']= form
	context['property_object'] = property_object
	if form.is_valid():
		form.save()
		return redirect('/propertydetail/%s/' %property_object.pk)
	return render (request,'owner_edit_property.html', context)

def add_image(request,pk):
	context = {}
	property_name = Property.objects.get(pk=pk)
	if property_name.owner != request.user:
		return redirect('/propertylist/')
	if request.method == 'POST':
		form = AddImageForm(request.POST, request.FILES)
		if form.is_valid():
			property_image = form.save(commit=False)
			property_image.property_object = property_name.user
			property_image.save()
			return redirect('/profile/')
	return render(request, 'add_image.html', context)
