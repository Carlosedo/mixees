from django.conf.urls import patterns, include, url
from django.contrib import admin
from apps.cocktails.views import IngredientListView, SpiritDetailView, MixerDetailView, SpiritCreateView
from apps.cocktails.views import MixerCreateView, CocktailListView, CocktailDetailView, CocktailCreateView
from apps.cocktails.views import CocktailUpdateView, IngredientCreateView, MixerIngredientCreateView, IngredientDeleteView
from apps.cocktails.views import MixerIngredientDeleteView

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^ingredients/$', IngredientListView.as_view(), name='ingredient_list'),
    url(r'^spirit/create$', SpiritCreateView.as_view(), name='spirit_create'),
    url(r'^mixer/create$', MixerCreateView.as_view(), name='mixer_create'),
    url(r'^spirit/(?P<slug>.+)$', SpiritDetailView.as_view(), name='spirit_detail'),
    url(r'^mixer/(?P<slug>.+)$', MixerDetailView.as_view(), name='mixer_detail'),
    url(r'^$', CocktailListView.as_view(), name='cocktail_list'),
    url(r'^(?P<slug>[-\w]+)$', CocktailDetailView.as_view(), name='cocktail_detail'),
    url(r'^new/$', CocktailCreateView.as_view(), name='cocktail_create'),
    url(r'^(?P<slug>[-\w]+)/update$', CocktailUpdateView.as_view(), name='cocktail_update'),
    url(r'^(?P<slug>[-\w]+)/add_ingredient/$', IngredientCreateView.as_view(), name='ingredient_create'),
    url(r'^(?P<slug>[-\w]+)/add_mixeringredient/$', MixerIngredientCreateView.as_view(), name='mixeringredient_create'),
    url(r'^(?P<slug>[-\w]+)/remove_ingredient/(?P<pk>\d+)/$', IngredientDeleteView.as_view(), name='ingredient_delete'),
    url(r'^(?P<slug>[-\w]+)/remove_mixeringredient/(?P<pk>\d+)/$', MixerIngredientDeleteView.as_view(), name='mixeringredient_delete'),
)
