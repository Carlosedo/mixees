from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse
from cocktails.models import Spirit, Mixer, Cocktail, Ingredient, MixerIngredient
from cocktails.forms import IngredientCreateForm, MixerIngredientCreateForm	



class IngredientListView(ListView):
	model = Spirit
	template_name = 'cocktails/ingredient_list.html'
	
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

class MixerCreateView(CreateView):
	model = Mixer

class CocktailListView(ListView):
	model = Cocktail

class CocktailDetailView(DetailView):
	model = Cocktail

class CocktailCreateView(CreateView):
	model = Cocktail

	def get_success_url(self):
		return reverse('ingredient_create', kwargs={'slug': self.object.slug})

class CocktailUpdateView(UpdateView):
	model = Cocktail
	template_name = "cocktails/cocktail_update_form.html"

class IngredientCreateView(CreateView):
	model = Ingredient
	form_class = IngredientCreateForm

	def get_form(self, form_class):
		form = super(IngredientCreateView, self).get_form(form_class)
		form.instance.cocktail = Cocktail.objects.get(slug=self.kwargs['slug'])
		return form

	def get_success_url(self):
		if '_addanother' in self.request.POST:
			return reverse('ingredient_create', kwargs={'slug': self.kwargs['slug']})
		return reverse('cocktail_detail', kwargs={'slug': self.kwargs['slug']})


class MixerIngredientCreateView(CreateView):
	model = MixerIngredient
	form_class = MixerIngredientCreateForm

	def get_form(self, form_class):
		form = super(MixerIngredientCreateView, self).get_form(form_class)
		form.instance.cocktail = Cocktail.objects.get(slug=self.kwargs['slug'])
		return form

	def get_success_url(self):
		if '_addanother' in self.request.POST:
			return reverse('mixeringredient_create', kwargs={'slug': self.kwargs['slug']})
		return reverse('cocktail_detail', kwargs={'slug': self.kwargs['slug']})


class IngredientDeleteView(DeleteView):
	model = Ingredient

	def get_success_url(self):
		return reverse('cocktail_detail', args=[self.kwargs['slug']])


class MixerIngredientDeleteView(DeleteView):
	model = MixerIngredient

	def get_success_url(self):
		return reverse('cocktail_detail', args=[self.kwargs['slug']])


