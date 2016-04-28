from django.shortcuts import render, redirect, render_to_response,get_object_or_404
from main.models import Property, PropertyImages, Schedule
from main.forms import AddPropertyForm, EditPropertyFrom, AddImageForm, OwnerAddScheduleForm
# Create your views here.
def user_book(request):
	context = {}

def owner_add_schedule(request):
	context = {}
	context['form'] = OwnerAddScheduleForm()

	if request.method == 'POST':
		form = OwnerAddScheduleForm(request.POST)
		if form.is_valid():
			schedule = form.save(commit=False)
			schedule.owner = request.user
			schedule.save()
			return redirect('/property_list/')
	return render(request,'owner_add_schedule.html', context)

def add_property(request):
	context = {}
	context['form'] = AddPropertyForm()
	if request.method == 'POST':
		form = AddPropertyForm(request.POST, request.FILES)

		if form.is_valid():
			property_object = form.save(commit=False)
			property_object.owner = request.user
			property_object.save()
			property_image = PropertyImages.objects.create(property_object=property_object)
			property_image.image = form.cleaned_data['img']
			property_image.save()
			
			return redirect('/profile/')
	return render(request, 'add_property.html', context)

def edit_property(request, pk):
	context = {}
	property_object = Property.objects.get(pk=pk)
	if property_object.owner != request.user:
		return redirect('/propertylist/')
	form = EditPropertyFrom(instance=property_object)
	context['form']= form
	context['property_object'] = property_object

	if request.method == 'POST':
		form = EditPropertyFrom (request.POST, request.FILES)

		context['form'] = form
		if form.is_valid():
			form.save(commit=False)
			property_image = PropertyImages.objects.create(property_object=property_object)
			property_image.image = form.cleaned_data['img']
			property_image.save()

			return redirect('/property_detail/%s/' %property_object.pk)
	return render (request,'owner_edit_property.html', context)


#must change that so we can add the image in the detail view
def add_image(request):
	context = {}
	context['form']= AddImageForm()
	# property_name = Property.objects.get(pk=pk)
	# if property_name.owner != request.user:
	# 	return redirect('/propertylist/')
	if request.method == 'POST':
		form = AddImageForm(request.POST, request.FILES)
		if form.is_valid():

			property_image = form.save(commit=False)
			property_image.save()
			return redirect('/profile/')
	return render(request, 'add_image.html', context)

def property_list(request):
	context = {}
	properties = Property.objects.all()
	context['properties'] = properties
	return render(request, 'properties_list.html', context)

def property_detail(request, pk):
	context = {}
	property_object = Property.objects.get(pk=pk)
	context['property']	= property_object
	return render(request,'property_detail.html', context)

