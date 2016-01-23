from django.views.generic import DetailView, CreateView, ListView
from django.core.urlresolvers import reverse

from apps.core.mixins import LoginRequiredMixin

from .models import Taste


class TasteDetailView(DetailView):
    model = Taste

    def get_context_data(self, **kwargs):
        context = super(TasteDetailView, self).get_context_data(**kwargs)

        taste = kwargs['object']
        context['cocktail_list'] = taste.cocktail_set.all()

        return context


class TasteCreateView(LoginRequiredMixin, CreateView):
    model = Taste
    fields = ['title']

    def get_success_url(self):
        return reverse(
            'taste_create',
            kwargs={
                'slug': self.object.slug
            }
        )

class TasteListView(ListView):
    model = Taste

    # TODO: To allow search
    def get_queryset(self):
        queryset = super(TasteListView, self).get_queryset()

        q = self.request.GET.get("q")
        if q:
            return queryset.filter(title__icontains=q).order_by('-views')
        return queryset.order_by('-views')
