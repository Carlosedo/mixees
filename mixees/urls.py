from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mixees.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    
    url(r'^$', 'apps.home.views.index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^cocktails/', include('apps.cocktails.urls')),
    url(r'^ingredients/', include('apps.ingredients.urls')),
)
