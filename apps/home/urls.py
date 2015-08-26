from django.conf.urls import patterns, url

from .views import IndexView, AboutView

urlpatterns = patterns('',
    url(r'^$', IndexView.as_view(), name='homepage'),
    url(r'^about/$', AboutView.as_view(), name='about'),
)
