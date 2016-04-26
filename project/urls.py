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
    url(r'^signup/$', 'main.views.sign_up'),
	url(r'^logout/$', 'main.views.logout_view'),
	url(r'^signin/$', 'main.views.login_view'),
	url(r'^profile/$', 'main.views.profile_page'),
  	url(r'^edit_profile/$', 'main.views.edit_profile'),

] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
