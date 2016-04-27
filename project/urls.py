from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'addproperty/$', 'main.views.add_property'),
    url(r'editproperty/(?P<pk>.+)/$', 'main.views.edit_property'),
    url(r'addimage/(?P<pk>.+)/$', 'main.views.add_image'),


]
