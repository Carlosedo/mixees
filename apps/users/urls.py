from django.conf.urls import patterns, url
from apps.users.views import CreateAccountView, UserProfileView

urlpatterns = patterns('',
    url(r'^register/$', CreateAccountView.as_view(), name='users.register'),
    url(r'^(?P<pk>\d+)/$', UserProfileView.as_view(), name='users.profile'),
)
