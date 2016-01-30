from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.decorators.csrf import csrf_exempt

from schema import schema
from graphene.contrib.django.views import GraphQLView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mixees.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'', include('apps.home.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^cocktails/', include('apps.cocktails.urls')),
    url(r'^ingredients/', include('apps.ingredients.urls')),
    url(r'^tastes/', include('apps.tastes.urls')),
    url(r'^users/', include('apps.users.urls')),

    url(r'^graphql', csrf_exempt(GraphQLView.as_view(schema=schema))),
    url(r'^graphiql', include('django_graphiql.urls')),

)

if settings.DEBUG:
    urlpatterns += patterns(
        'django.views.static',
        (r'^media/(?P<path>.*)',
        'serve',
        {'document_root': settings.MEDIA_ROOT}), )