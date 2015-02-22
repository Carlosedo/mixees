from django.contrib import admin
from cocktails.models import Spirit, Mixer, Cocktail, Ingredient

admin.site.register(Spirit)
admin.site.register(Mixer)
admin.site.register(Cocktail)

class IngredientAdmin(admin.ModelAdmin):
    list_display = ('spirits', 'amount', 'measurement', 'cocktail')

admin.site.register(Ingredient, IngredientAdmin)