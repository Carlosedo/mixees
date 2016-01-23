from django.conf.urls import patterns, url
from .views import TasteDetailView, TasteCreateView, TasteListView

urlpatterns = patterns('',
    url(r'^$', TasteListView.as_view(), name='taste_list'),
    url(r'^create/$', TasteCreateView.as_view(), name='taste_create'),
    url(r'^(?P<slug>.+)/$', TasteDetailView.as_view(), name='taste_detail'),
)