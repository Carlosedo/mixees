from django.forms import ModelForm
from apps.ingredients.models import Ingredient, MixerIngredient

class IngredientCreateForm(ModelForm):
    class Meta:
        model = Ingredient
        exclude = ['cocktail']


class MixerIngredientCreateForm(ModelForm):
    class Meta:
        model = MixerIngredient
        exclude = ['cocktail']