from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.core.urlresolvers import reverse

from apps.cocktails.models import Cocktail
from apps.ingredients.models import Spirit, Mixer


class CocktailListView(ListView):
    model = Cocktail

    def get_queryset(self):
        queryset = super(CocktailListView, self).get_queryset()

        q = self.request.GET.get("q")
        if q:
            return queryset.filter(title__icontains=q)
        return queryset


class CocktailDetailView(DetailView):
    model = Cocktail

    def get_context_data(self, **kwargs):
        context = super(CocktailDetailView, self).get_context_data(**kwargs)

        cocktail = kwargs['object']
        ingredients = cocktail.ingredient_set.all()

        context['spirits'] = ingredients.filter(liquid=Spirit)
        context['mixers'] = ingredients.filter(liquid=Mixer)
        return context


class CocktailCreateView(CreateView):
    model = Cocktail
    fields = ['title', 'slug', 'description']

    def get_success_url(self):
        return reverse('ingredient_create', kwargs={'slug': self.object.slug})


class CocktailUpdateView(UpdateView):
    model = Cocktail
    template_name = "cocktails/cocktail_update_form.html"
    fields = ['description']



