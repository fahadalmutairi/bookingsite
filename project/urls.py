from django.conf.urls import include, url
from django.contrib import admin
from main import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^property_list/$', 'main.views.property_list'),
    url(r'^property_detail/(?P<pk>[0-9]+)/$', 'main.views.property_detail'),
]
