from django.shortcuts import render

# Create your views here.

def property_list(request):
	context = {}
	properties = Property.objects.all()
	# property_image = Ima
	context['properties'] = properties
	return render(request, 'properties_list.html', context)

def property_detail(request, pk):
	context = {}
	property_object = Property.object.get(pk=pk)
	context['property']	= property_object
	return render(request,'property_detail.html', context)

