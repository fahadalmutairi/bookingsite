from main.forms import BookingForm, FilterTime, CustomUserCreationForm, CustomUserLoginForm, EditProfileForm, AreaSearchForm, AddPropertyForm, EditPropertyFrom,AddImageForm, OwnerAddScheduleForm  , CheckForm
from django.contrib.auth import authenticate, login, logout
from django.utils.html import escape
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect, render_to_response,get_object_or_404
from main.models import Property, PropertyImages, Schedule, CustomUser, Property, PropertyImages, Booking, Schedule_2
from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse , Http404, HttpResponseRedirect 
from datetime import datetime
from itertools import chain
from django.db.models import Q
import requests
# Create your views here.


def become_owner(request):
    request.user.is_owner = True 
    request.user.save()
    r = send_simple_message(request.user,"Congratulations..", "You become an approved property owner")
    print r.text
    return render(request, 'become_owner.html')


def user_book(request):
    context = {}


def owner_add_schedule(request, pk):
    context = {}
    context['form'] = OwnerAddScheduleForm()
    prop = Property.objects.get(pk=pk)
    context['prop'] = prop

    if request.method == 'POST':
        form = OwnerAddScheduleForm(request.POST)
        if form.is_valid():
            schedule = form.save(commit=False)
            schedule.owner = request.user
            schedule.property_object = prop
            schedule.save()
            return redirect('/property_list/')
    return render(request, 'owner_add_schedule.html', context)


def area_search(request):
	request_context = RequestContext(request)
	context = {}
	if request.method == 'POST':
		form = AreaSearchForm(request.POST)
		context['form'] = form

		if form.is_valid():
			name = '%s' % form.cleaned_data['area']
			context['property_list'] = Property.objects.filter(address__area__icontains=name)
			return render_to_response('search_page.html', context, context_instance=request_context)
		else:
			context['valid'] = form.errors
			return render_to_response('search_page.html', context, context_instance=request_context)
	else:
		form = AreaSearchForm()
		context['form']	= form
		return render_to_response('search_page.html', context, context_instance=request_context)



def type_search(request):
    context = {}

    try:
        context['property_list'] = Property.objects.filter(type =request.user.pk)
    except Exception, e:
        raise Http404('404')
    
    return render_to_response(request, 'property_list.html', context)
   



def filter(request):
	context = {}
	if request.method == 'POST':


		form = FilterTime(request.POST)
		context['form'] = form

		if form.is_valid():
			start = form.cleaned_data['start']
			end = form.cleaned_data['end']
			startsearch = Q(date_start__lte=start , date_end__gt=start)
			endsearch = Q(date_start__lt=end , date_end__gte=end)
			context['date_start'] = Schedule.objects.filter(startsearch & endsearch)
			return render(request,'filter.html', context)
		else:
			context['valid'] = form.errors
			return render(request,'filter.html', context)
	else:
		form = FilterTime()
		context['form'] = form

		return render(request,'filter.html', context)

	return render(request,'filter.html', context)


def create_booking(request, pk):

	booking_dict = request.GET

	print request.GET

	start_date = request.GET.get('start_date', None)
	end_date = request.GET.get('end_date', None)
	s_pk = request.GET.get('s_pk', None)
	owner = request.GET.get('owner', None)
	property_object = request.GET.get('property_object', None)

	booking, created = Booking.objects.get_or_create(user=request.user, schedule=Schedule.objects.get(pk=s_pk))

	booking.booked = True

	booking.date_start = start_date
	booking.date_end = end_date
	booking.owner = CustomUser.objects.get(email=owner)
	booking.property_object = Property.objects.get(pk=property_object)


	booking.save()

	if booking:
		return redirect('/profile/')


	return HttpResponse('fail')

	

def owner_add_schedule(request,pk):
	context = {}
	context['form'] = OwnerAddScheduleForm()
	prop = Property.objects.get(pk=pk)
	context['prop'] = prop

	if request.method == 'POST':
		form = OwnerAddScheduleForm(request.POST)
		if form.is_valid():
			schedule = form.save(commit=False)
			schedule.owner = request.user
			schedule.property_object = prop
			schedule.save()
			return redirect('/property_list/')
	return render(request,'owner_add_schedule.html', context)


def edit_profile(request):
    context = {}
    try:
        user = CustomUser.objects.get(pk=request.user.pk)
    except Exception, e:
        raise Http404('404')

    form = EditProfileForm(request.POST or None, instance=user)
    context['form'] = form

    if form.is_valid():
        form.save()
        return redirect('/profile/')
    else:
        print form.errors

    return render(request, 'edit_profile.html', context)


@login_required
def profile_page(request):
    context = {}
    print request.user
    if request.user.is_owner:
        properties = request.user.property_set.all()
        context['property'] = properties
    else:
        pass
    context['user'] = CustomUser.objects.get(pk=request.user.pk)
    return render(request, 'profile_page.html', context)


def sign_up(request):
    context = {}
    context['form'] = CustomUserCreationForm()

    if request.method == 'POST':

        form = CustomUserCreationForm(request.POST)
        context['form'] = form

        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email', None)
            password = form.cleaned_data.get('password1', None)
            auth_user = authenticate(username=email, password=password)

            try:
                login(request, auth_user)
                r = send_simple_message(email, "Welcome and Thanks" , "You have successfully signed up to Bookingsite.")
                print r.text
            except Exception, e:
                print e
                return HttpResponse('invalid user, try again <a href="/signup/">here</a>')
    return render(request, 'signup.html', context)


def login_view(request):
    context = {}

    context['form'] = CustomUserLoginForm()

    if request.method == 'POST':

        form = CustomUserLoginForm(request.POST)
        context['form'] = form

        if form.is_valid():
            email = form.cleaned_data.get('email', None)
            password = form.cleaned_data.get('password', None)
            auth_user = authenticate(username=email, password=password)

            try:
                login(request, auth_user)
            except Exception, e:
                message = """
				username or password incorrect, try again
				<a href='/signin/'> login</a>
				"""
                return HttpResponse(message)
    return render(request, 'signin.html', context)


def logout_view(request):
    logout(request)
    return redirect('/')


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
        return redirect('/property_list/')
    form = EditPropertyFrom(instance=property_object)
    context['form'] = form
    context['property_object'] = property_object

    if request.method == 'POST':
        form = EditPropertyFrom(request.POST, request.FILES)

        context['form'] = form
        if form.is_valid():
            form.save(commit=False)
            property_image = PropertyImages.objects.create(property_object=property_object)
            property_image.image = form.cleaned_data['img']
            property_image.save()

            return redirect('/property_detail/%s/' % property_object.pk)
    return render(request, 'owner_edit_property.html', context)


# must change that so we can add the image in the detail view
def add_image(request, pk):
    context = {}
    context['form'] = AddImageForm()
    property_name = Property.objects.get(pk=pk)
    context['property'] = property_name
    # if property_name.owner != request.user:
    # 	return redirect('/propertylist/')
    if request.method == 'POST':
        form = AddImageForm(request.POST, request.FILES)
        if form.is_valid():
            property_image = form.save(commit=False)
            property_image.property_object = property_name
            property_image.save()
            return redirect('/property_detail/%s/' % property_name.pk)
    return render(request, 'add_image.html', context)


def property_list(request):
    context = {}
    properties = Property.objects.all()
    context['properties'] = properties
    return render(request, 'properties_list.html', context)


def property_detail(request, pk):
    context = {}
    property_object = Property.objects.get(pk=pk)
    context['property'] = property_object
    other_properties = Property.objects.filter(address__area=property_object.address.area)
    context['other_properties'] = other_properties
    return render(request, 'property_detail.html', context)


def area_search(request):
    request_context = RequestContext(request)
    context = {}
    if request.method == 'POST':
        form = AreaSearchForm(request.POST)
        context['form'] = form

        if form.is_valid():
            name = '%s' % form.cleaned_data['area']
            context['property_list'] = Property.objects.filter(address__area__icontains=name)
            return render_to_response('search_page.html', context, context_instance=request_context)
        else:
            context['valid'] = form.errors
            return render_to_response('search_page.html', context, context_instance=request_context)
    else:
        form = AreaSearchForm()
        context['form'] = form
        return render_to_response('search_page.html', context, context_instance=request_context)


def chalets(request):
    context = {}
    chalets = Property.objects.filter(property_type_choices__icontains='chalet')
    context['chalets'] = chalets
    return render(request, 'chalets.html', context)

def farms(request):
    context = {}
    farms = Property.objects.filter(property_type_choices__icontains='farm')
    context['farms'] = farms
    return render(request, 'farms.html', context)

def apartments(request):
    context = {}
    apartments = Property.objects.filter(property_type_choices__icontains='apartment')
    context['apartments'] = apartments
    return render(request, 'apartments.html', context)

		
def index(request):
    request_context = RequestContext(request)
    context = {}
    if request.method == 'POST':
        form = AreaSearchForm(request.POST)
        context['form'] = form

        if form.is_valid():
            name = '%s' % form.cleaned_data['area']
            context['property_list'] = Property.objects.filter(address__area__icontains=name)
            return render_to_response('index.html', context, context_instance=request_context)
        else:
            context['valid'] = form.errors
            return render_to_response('index.html', context, context_instance=request_context)
    else:
        form = AreaSearchForm()
        context['form'] = form
        return render_to_response('index.html', context, context_instance=request_context)


 
def send_simple_message(to, sub, text):
    return requests.post(
        "https://api.mailgun.net/v3/samples.mailgun.org/messages",
        auth=("api", "key-3ax6xnjp29jd6fds4gc373sgvjxteol0"),
        data={"from": "BookingSite.com <excited@samples.mailgun.org>",
              "to": [to, ],
              "subject": sub ,
              "text": text })

