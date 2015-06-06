from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse

from apps.ingredients.models import Spirit, Mixer, Ingredient, MixerIngredient
from apps.cocktails.models import Cocktail
from apps.ingredients.forms import IngredientCreateForm, MixerIngredientCreateForm


class IngredientListView(ListView):
    model = Spirit
    template_name = 'ingredients/ingredient_list.html'
    
    def get_context_data(self, **kwargs):
        context = super(IngredientListView, self).get_context_data(**kwargs)
        context['mixers'] = Mixer.objects.all()
        return context


class SpiritDetailView(DetailView):
    model = Spirit


class MixerDetailView(DetailView):
    model = Mixer


class SpiritCreateView(CreateView):
    model = Spirit
    fields =['name', 'slug']


class MixerCreateView(CreateView):
    model = Mixer
    fields =['name', 'slug']


class IngredientCreateView(CreateView):
    model = Ingredient
    form_class = IngredientCreateForm

    def get_form(self, form_class):
        form = super(IngredientCreateView, self).get_form(form_class)
        form.instance.cocktail = Cocktail.objects.get(slug=self.kwargs['slug'])
        return form

    def get_success_url(self):
        if '_addspirit' in self.request.POST:
            return reverse('ingredient_create', kwargs={'slug': self.kwargs['slug']})
        elif '_addmixer' in self.request.POST:
            return reverse('mixeringredient_create', kwargs={'slug': self.kwargs['slug']})
        return reverse('cocktail_detail', kwargs={'slug': self.kwargs['slug']})


class MixerIngredientCreateView(CreateView):
    model = MixerIngredient
    form_class = MixerIngredientCreateForm

    def get_form(self, form_class):
        form = super(MixerIngredientCreateView, self).get_form(form_class)
        form.instance.cocktail = Cocktail.objects.get(slug=self.kwargs['slug'])
        return form

    def get_success_url(self):
        if '_addspirit' in self.request.POST:
            return reverse('ingredient_create', kwargs={'slug': self.kwargs['slug']})
        elif '_addmixer' in self.request.POST:
            return reverse('mixeringredient_create', kwargs={'slug': self.kwargs['slug']})
        return reverse('cocktail_detail', kwargs={'slug': self.kwargs['slug']})


class DeleteMixin(object):
    """Adds successful url functionality to DeleteViews"""
    
    def get_success_url(self):
        return reverse('cocktail_detail', args=[self.kwargs['slug']])
        

class IngredientDeleteView(DeleteMixin, DeleteView):
    model = Ingredient


class MixerIngredientDeleteView(DeleteMixin, DeleteView):
    model = MixerIngredient
    template_name="ingredients/ingredient_confirm_delete.html"


