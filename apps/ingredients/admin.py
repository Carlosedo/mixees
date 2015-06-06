from django.contrib import admin

from apps.ingredients.models import Spirit, Mixer, Ingredient

admin.site.register(Spirit)
admin.site.register(Mixer)

class IngredientAdmin(admin.ModelAdmin):
    list_display = ('spirits', 'amount', 'measurement', 'cocktail')

admin.site.register(Ingredient, IngredientAdmin)