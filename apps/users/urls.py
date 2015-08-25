from django.conf.urls import patterns, url
from apps.users.views import CreateAccountView, LoginView, UserProfileView, user_logout

urlpatterns = patterns('',
    url(r'^register/$', CreateAccountView.as_view(), name='users.register'),
    url(r'^login/$', LoginView.as_view(), name='users.login'),
    url(r'^logout/$', user_logout, name='users.logout'),
    url(r'^(?P<pk>\d+)/$', UserProfileView.as_view(), name='users.profile'),
)
