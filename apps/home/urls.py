from django.conf.urls import patterns, url

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mixees.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    
    url(r'^$', 'apps.home.views.index'),
    url(r'^about/$', 'apps.home.views.about'),
)
