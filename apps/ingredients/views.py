from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse
from django.forms import HiddenInput

from apps.ingredients.models import Spirit, Mixer, Ingredient
from apps.cocktails.models import Cocktail
from apps.ingredients.forms import IngredientCreateForm 


class IngredientListView(ListView):
    template_name = 'ingredients/ingredient_list.html'
    
    def get_context_data(self, **kwargs):
        context = super(IngredientListView, self).get_context_data(**kwargs)
        context['spirits'] = Spirit.objects.all()
        context['mixers'] = Mixer.objects.all()
        return context


class SpiritDetailView(DetailView):
    model = Spirit


class MixerDetailView(DetailView):
    model = Mixer


class SpiritCreateView(CreateView):
    model = Spirit
    fields =['name', 'volume']


class MixerCreateView(CreateView):
    model = Mixer
    fields =['name']


class IngredientCreateView(CreateView):
    model = Ingredient
    form_class = IngredientCreateForm

    def get_form(self, form_class):
        form = super(IngredientCreateView, self).get_form(form_class)
        form.instance.cocktail = Cocktail.objects.get(slug=self.kwargs['slug'])

        if self.kwargs['type'] == 'spirit':
            form.fields['mixer'].widget = HiddenInput()
        elif self.kwargs['type'] == 'mixer':
            form.fields['spirit'].widget = HiddenInput()

        return form

    def get_context_data(self, **kwargs):
        context = super(IngredientCreateView, self).get_context_data(**kwargs)
        context['ingredient_type'] = self.kwargs['type']
        return context

    def get_success_url(self):
        if '_addspirit' in self.request.POST:
            return reverse(
                'ingredient_create',
                kwargs={
                    'slug': self.kwargs['slug'],
                    'type': 'spirit'
                }
            )
        elif '_addmixer' in self.request.POST:
            return reverse(
                'ingredient_create',
                kwargs={
                    'slug': self.kwargs['slug'],
                    'type': 'mixer'
                }
            )
        return reverse('cocktail_detail', kwargs={'slug': self.kwargs['slug']})


class DeleteMixin(object):
    """Adds successful url functionality to DeleteViews"""
    
    def get_success_url(self):
        return reverse('cocktail_detail', args=[self.kwargs['slug']])
        

class IngredientDeleteView(DeleteMixin, DeleteView):
    model = Ingredient
    template_name="ingredients/ingredient_confirm_delete.html"


