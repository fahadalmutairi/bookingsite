from django.shortcuts import render , render_to_response, redirect , get_object_or_404
from main.models import  CustomUser, Property
from main.forms import CustomUserCreationForm , CustomUserLoginForm ,  EditProfileForm ,AddPropertyForm, EditPropertyFrom
from django.template import RequestContext
from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse , Http404, HttpResponseRedirect 
from django.contrib.auth.decorators import login_required


# Create your views here.


def edit_profile(request):
	context = {}
	try:
		user =CustomUser.objects.get(pk=request.user.pk) 
	except Exception, e :
		raise Http404('404')

	form= EditProfileForm(request.POST or None, instance=user)
	context['form'] =form

	if form.is_valid():
		form.save()
		return redirect ('/profile/')
	else:
		print form.errors

	return render(request,'edit_profile.html', context)


@login_required
def profile_page(request):
	context={}
	print request.user
	if request.user.is_owner :
		properties = request.user.property_set.all()
		context['property']= properties
	else:			
		pass
	context['user']= CustomUser.objects.get(pk=request.user.pk)
	return render(request,'profile_page.html', context)


def sign_up(request):
	context ={}
	context['form'] = CustomUserCreationForm()

	if request.method =='POST':
		
		form=CustomUserCreationForm(request.POST)
		context['form'] = form

		if form.is_valid():
			form.save()
			email = form.cleaned_data.get('email',None)
			password = form.cleaned_data.get('password1',None)
			auth_user = authenticate(username=email, password=password)

			try:
				login(request, auth_user)
			except Exception, e:
				print e 
				return HttpResponse('invalid user, try again <a href="/signup/">here</a>')
			
	return render (request,'signup.html',context)


def login_view(request):

	context={}

	context['form'] =CustomUserLoginForm()

	if request.method == 'POST':

		form = CustomUserLoginForm(request.POST)
		context['form'] = form

		if form.is_valid(): 
			email = form.cleaned_data.get('email',None)
			password= form.cleaned_data.get('password',None)
			auth_user = authenticate(username=email, password=password)

			try:
				login(request, auth_user)

			except Exception, e:
				message= """
				username or password incorrect, try again
				<a href='/signin/'> login</a>
				"""
				return HttpResponse(message)
	return render (request, 'signin.html', context)


def logout_view(request):
	logout(request)
	return redirect('/signup/')


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

def property_list(request):
	context = {}
	properties = Property.objects.all()
	context['properties'] = properties
	return render(request, 'properties_list.html', context)

def property_detail(request, pk):
	context = {}
	property_object = Property.object.get(pk=pk)
	context['property']	= property_object
	return render(request,'property_detail.html', context)

