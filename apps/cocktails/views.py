from django.views.generic import (
    View, ListView, DetailView, CreateView, UpdateView, DeleteView
)
from django.core.urlresolvers import reverse

from apps.core.mixins import LoginRequiredMixin
from apps.ingredients.models import Spirit, Mixer
from apps.users.models import UserProfile
from .models import Cocktail

from braces.views import AjaxResponseMixin, JSONResponseMixin


class CocktailListView(ListView):
    model = Cocktail

    def get_queryset(self):
        queryset = super(CocktailListView, self).get_queryset()

        q = self.request.GET.get("q")
        if q:
            return queryset.filter(title__icontains=q).order_by('-views')
        return queryset.order_by('-views')


class CocktailDetailView(DetailView):
    model = Cocktail

    def get_context_data(self, **kwargs):
        context = super(CocktailDetailView, self).get_context_data(**kwargs)

        cocktail = kwargs['object']

        context['spirit_ingredients'] = cocktail.ingredient_set.all().exclude(spirit__isnull=True)
        context['mixer_ingredients'] = cocktail.ingredient_set.all().exclude(mixer__isnull=True)

        context['spirits'] = []
        for ingredient in context['spirit_ingredients']:
            context['spirits'].append({
                'measurement': ingredient.measurement,
                'amount': ingredient.amount,
                'ingredient': ingredient.spirit.slug
            })

        context['mixers'] = []
        for ingredient in context['mixer_ingredients']:
            context['mixers'].append({
                'measurement': ingredient.measurement,
                'amount': ingredient.amount,
                'ingredient': ingredient.mixer.slug
            })

        context['total_parts'] = cocktail.total_parts

        cocktail.views += 1
        cocktail.save()

        users_who_liked = UserProfile.objects.filter(liked_cocktails__slug=cocktail.slug)
        context['likes'] = users_who_liked.count()

        if self.request.user.is_authenticated():
            user = UserProfile.objects.get(user__id=self.request.user.id)
            context['liked_by_user'] = 1 if user in users_who_liked else 0

        return context


class CocktailCreateView(LoginRequiredMixin, CreateView):
    model = Cocktail
    fields = ['title', 'description', 'tastes']

    def get_success_url(self):
        return reverse(
            'ingredient_create',
            kwargs={
                'slug': self.object.slug,
                'type': 'spirit'
            }
        )


class CocktailUpdateView(LoginRequiredMixin, UpdateView):
    model = Cocktail
    template_name = "cocktails/cocktail_update_form.html"
    fields = ['description']


class CocktailDeleteView(DeleteView):
    model = Cocktail
    template_name = "cocktails/cocktail_confirm_delete.html"

    def get_success_url(self):
        return reverse('cocktail_list')


class CocktailLikeView(JSONResponseMixin, AjaxResponseMixin, View):
    def get_ajax(self, request, *args, **kwargs):
        cocktail_id = request.GET['cocktail_id']
        already_liked = bool(int(request.GET['already_liked']))
        user_id = request.user.id

        if cocktail_id and user_id:
            cocktail = Cocktail.objects.get(id=int(cocktail_id))
            user = UserProfile.objects.get(id=int(user_id))

            if already_liked:
                user.liked_cocktails.remove(cocktail)
            else:
                user.liked_cocktails.add(cocktail)


        return self.render_json_response({
            'likes': UserProfile.objects.filter(liked_cocktails__slug=cocktail.slug).count(),
            'liked_by_user': 0 if already_liked else 1
        })
