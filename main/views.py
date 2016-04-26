from django.shortcuts import render , render_to_response, redirect , get_object_or_404
from main.models import  CustomUser
from main.forms import CustomUserCreationForm , CustomUserLoginForm ,  EditProfileForm
from django.template import RequestContext
from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse , Http404, HttpResponseRedirect 


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


def profile_page(request):
	context={}
	print request.user
	print request.user.pk
	try:
		context['user'] =CustomUser.objects.get(pk=request.user.pk)
	except Exception, e :
		raise Http404('404')
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