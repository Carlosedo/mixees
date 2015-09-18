from apps.cocktails.models import Cocktail
from apps.ingredients.models import Liquid, Spirit, Mixer, Ingredient


def add_spirit(name, volume):
    s = Spirit.objects.get_or_create(
        name=name,
        volume=volume
    )[0]
    return s

def add_mixer(name):
    m = Mixer.objects.get_or_create(
        name=name,
    )[0]
    return m

def add_cocktail(title, description, views=0):
    c = Cocktail.objects.get_or_create(
        title=title,
        description = description,
        views = views
    )[0]
    return c

def add_ingredient(cocktail, amount, measurement, spirit=None, mixer=None):
    i = Ingredient.objects.get_or_create(
        cocktail=cocktail,
        amount=amount,
        measurement=measurement,
        spirit=spirit,
        mixer=mixer
    )[0]
    i.save()
    return i
