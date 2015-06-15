import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mixees.settings')

import django
django.setup()

from apps.cocktails.models import Cocktail
from apps.ingredients.models import Liquid, Spirit, Mixer, Ingredient


def populate():
    rum = add_spirit('Rum', 'rum', 39)
    vodka = add_spirit('Vodka', 'vodka', 40)
    gin = add_spirit('Gin', 'gin', 42)
    whiskey = add_spirit('Whiskey', 'whiskey', 40)

    coke = add_mixer('Coke', 'coke')
    orange = add_mixer('Orange', 'orange')
    tonic = add_mixer('Tonic', 'tonic')
    red_bull = add_mixer('Red Bull', 'red-bull')

    cuba_libre = add_cocktail(
        title='Cuba Libre',
        slug='cuba-libre',
        description='Typical cuban drink',
        likes=10,
    )

    gin_tonic = add_cocktail(
        title='Gin and Tonic',
        slug='gin-and-tonic',
        description='Fashionable drink',
        likes=5,
    )

    screwdriver = add_cocktail(
        title='Screwdriver',
        slug='screwdriver',
        description='Fresh vodka drink',
    )

    wings = add_cocktail(
        title='Wings',
        slug='wings',
        description='This drink gives you wings',
    )

    vodka_gin = add_cocktail(
        title='Vodka Gintini',
        slug='vodka-gintini',
        description='Vodka Martini with a twist',
        likes=7,
    )

    add_ingredient(
        cocktail=cuba_libre,
        amount=1,
        measurement=4,
        spirit=rum
    )

    add_ingredient(
        cocktail=cuba_libre,
        amount=2,
        measurement=4,
        mixer=coke
    )

    add_ingredient(
        cocktail=gin_tonic,
        amount=100,
        measurement=1,
        spirit=gin
    )

    add_ingredient(
        cocktail=gin_tonic,
        amount=200,
        measurement=1,
        mixer=tonic
    )

    add_ingredient(
        cocktail=screwdriver,
        amount=3,
        measurement=2,
        spirit=vodka
    )

    add_ingredient(
        cocktail=screwdriver,
        amount=6,
        measurement=2,
        mixer=orange
    )

    add_ingredient(
        cocktail=wings,
        amount=1,
        measurement=3,
        spirit=whiskey
    )

    add_ingredient(
        cocktail=wings,
        amount=1,
        measurement=3,
        mixer=red_bull
    )

    add_ingredient(
        cocktail=vodka_gin,
        amount=100,
        measurement=1,
        spirit=vodka
    )

    add_ingredient(
        cocktail=vodka_gin,
        amount=3,
        measurement=5,
        spirit=gin
    )

    # Print out what we have added to the user.
    for c in Cocktail.objects.all():
        for i in c.ingredient_set.all():
            print "- {0} - {1}".format(str(c), str(i))


def add_spirit(name, slug, volume):
    s = Spirit.objects.get_or_create(
        name=name,
        slug=slug,
        volume=volume
    )[0]
    return s

def add_mixer(name, slug):
    m = Mixer.objects.get_or_create(
        name=name,
        slug=slug
    )[0]
    return m

def add_cocktail(title, slug, description, views=0, likes=0):
    c = Cocktail.objects.get_or_create(
        title=title,
        slug = slug,
        description = description,
        views = views,
        likes = likes
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

# Start execution here!
if __name__ == '__main__':
    print "Starting Mixees population script..."
    populate()