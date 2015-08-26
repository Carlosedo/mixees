from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.core.urlresolvers import reverse

from apps.core.mixins import LoginRequiredMixin
from apps.cocktails.models import Cocktail
from apps.ingredients.models import Spirit, Mixer


class CocktailListView(ListView):
    model = Cocktail

    def get_queryset(self):
        queryset = super(CocktailListView, self).get_queryset()

        q = self.request.GET.get("q")
        if q:
            return queryset.filter(title__icontains=q).order_by('-likes')
        return queryset.order_by('-likes')


class CocktailDetailView(DetailView):
    model = Cocktail

    def get_context_data(self, **kwargs):
        context = super(CocktailDetailView, self).get_context_data(**kwargs)

        cocktail = kwargs['object']
        ingredients = cocktail.ingredient_set.all()

        context['spirits'] = ingredients.exclude(spirit__isnull=True)
        context['mixers'] = ingredients.exclude(mixer__isnull=True)

        # context['spirits'] = Spirit.objects.filter(
        #     id__in=ingredients.values_list('spirit', flat=True)
        # )
        # import ipdb; ipdb.set_trace()
        # context['mixers'] = Mixer.objects.filter(
        #     id__in=ingredients.values_list('mixer', flat=True)
        # )
        return context


class CocktailCreateView(LoginRequiredMixin, CreateView):
    model = Cocktail
    fields = ['title', 'description']

    def get_success_url(self):
        return reverse('ingredient_create', kwargs={'slug': self.object.slug})


class CocktailUpdateView(LoginRequiredMixin, UpdateView):
    model = Cocktail
    template_name = "cocktails/cocktail_update_form.html"
    fields = ['description']



