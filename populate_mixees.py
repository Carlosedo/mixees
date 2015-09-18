import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mixees.settings')

import django
django.setup()

from apps.core.populate_helpers import add_spirit, add_mixer, add_cocktail, add_ingredient
from apps.cocktails.models import Cocktail


def populate():
    rum = add_spirit('Rum', 39)
    vodka = add_spirit('Vodka', 40)
    gin = add_spirit('Gin', 42)
    whiskey = add_spirit('Whiskey', 40)

    coke = add_mixer('Coke')
    orange = add_mixer('Orange')
    tonic = add_mixer('Tonic')
    red_bull = add_mixer('Red Bull')

    cuba_libre = add_cocktail(
        title='Cuba Libre',
        description='Typical cuban drink',
        views=10,
    )

    gin_tonic = add_cocktail(
        title='Gin and Tonic',
        description='Fashionable drink',
        views=5,
    )

    screwdriver = add_cocktail(
        title='Screwdriver',
        description='Fresh vodka drink',
    )

    wings = add_cocktail(
        title='Wings',
        description='This drink gives you wings',
    )

    vodka_gin = add_cocktail(
        title='Vodka Gintini',
        description='Vodka Martini with a twist',
        views=7,
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


# Start execution here!
if __name__ == '__main__':
    print "Starting Mixees population script..."
    populate()
