from django.forms import ModelForm
from apps.ingredients.models import Ingredient


class IngredientCreateForm(ModelForm):
    class Meta:
        model = Ingredient
        fields = ['amount', 'measurement', 'spirit', 'mixer']