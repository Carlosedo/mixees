from django.conf.urls import patterns, include, url
from django.contrib import admin

from .views import (
    CocktailListView, CocktailDetailView, CocktailCreateView, CocktailUpdateView,
    CocktailLikeView
)


urlpatterns = [
    url(r'^$', CocktailListView.as_view(), name='cocktail_list'),
    url(r'^(?P<slug>[-\w]+)$', CocktailDetailView.as_view(), name='cocktail_detail'),
    url(r'^new/$', CocktailCreateView.as_view(), name='cocktail_create'),
    url(r'^(?P<slug>[-\w]+)/update$', CocktailUpdateView.as_view(), name='cocktail_update'),
    url(r'^like-cocktail/$', CocktailLikeView.as_view(), name='cocktail_like'),
]
