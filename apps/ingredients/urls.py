from django.conf.urls import patterns, include, url
from django.contrib import admin
from apps.ingredients.views import IngredientListView, SpiritDetailView, MixerDetailView, SpiritCreateView
from apps.ingredients.views import MixerCreateView, IngredientCreateView, IngredientDeleteView

urlpatterns = patterns('',
    url(r'^$', IngredientListView.as_view(), name='ingredient_list'),
    url(r'^spirit/create/$', SpiritCreateView.as_view(), name='spirit_create'),
    url(r'^mixer/create/$', MixerCreateView.as_view(), name='mixer_create'),
    url(r'^spirit/(?P<slug>.+)/$', SpiritDetailView.as_view(), name='spirit_detail'),
    url(r'^mixer/(?P<slug>.+)/$', MixerDetailView.as_view(), name='mixer_detail'),
    url(r'^(?P<slug>[-\w]+)/add_(?P<type>[-\w]+)/$', IngredientCreateView.as_view(), name='ingredient_create'),
    url(r'^(?P<slug>[-\w]+)/remove_ingredient/(?P<pk>\d+)/$', IngredientDeleteView.as_view(), name='ingredient_delete'),
)