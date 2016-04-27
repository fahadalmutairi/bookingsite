from django.shortcuts import render, render_to_response
from main.models import Property
from main.forms import AreaSearchForm
from django.utils.html import escape
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.views.decorators.csrf import csrf_exempt


# Create your views here.

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
