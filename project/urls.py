from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from main import views
from django.conf.urls.static import static


urlpatterns = [
    # Examples:
    # url(r'^$', 'project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),


    url(r'^addproperty/$', 'main.views.add_property'),
    url(r'^editproperty/(?P<pk>.+)/$', 'main.views.edit_property'),
    url(r'^addimage/$', 'main.views.add_image'),

    url(r'^signup/$', 'main.views.sign_up'),
	url(r'^logout/$', 'main.views.logout_view'),
	url(r'^signin/$', 'main.views.login_view'),
	url(r'^profile/$', 'main.views.profile_page'),
  	url(r'^edit_profile/$', 'main.views.edit_profile'),

    url(r'addproperty/$', 'main.views.add_property'),
    url(r'editproperty/(?P<pk>.+)/$', 'main.views.edit_property'),
    url(r'addimage/(?P<pk>.+)/$', 'main.views.add_image'),

    url(r'^property_list/$', 'main.views.property_list'),
    url(r'^property_detail/(?P<pk>[0-9]+)/$', 'main.views.property_detail'),

    url(r'^ownerschedule/(?P<pk>[0-9]+)/$', 'main.views.owner_add_schedule'),


    url(r'^search/$','main.views.area_search')
    
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

