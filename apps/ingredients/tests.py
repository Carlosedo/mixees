from django.test import TestCase

from apps.core.populate_helpers import add_spirit, add_mixer, add_cocktail, add_ingredient
from apps.cocktails.models import Cocktail
from .models import Liquid, Spirit, Mixer, Ingredient


class LiquidsModelTest(TestCase):

    def test_saving_and_retrieving_items(self):
        spirit = add_spirit('Ron Brugal', 40)

        mixer = add_mixer('Coca cola')

        _cocktail = Cocktail(title='Cuba Libre')
        _cocktail.save()

        mixer_ingredient = add_ingredient(_cocktail, 1, 2, mixer=mixer)

        spirit_ingredient = add_ingredient(_cocktail, 1, 2, spirit=spirit)

        saved_spirit = Spirit.objects.all()
        saved_mixer = Mixer.objects.all()
        saved_mixer_ingredient = Ingredient.objects.filter(spirit__isnull=True)
        saved_spirit_ingredient = Ingredient.objects.filter(mixer__isnull=True)

        self.assertEqual(len(saved_spirit), 1)
        self.assertEqual(saved_spirit[0].name, 'Ron Brugal')
        self.assertEqual(saved_spirit[0].volume, 40)

        self.assertEqual(len(saved_mixer), 1)
        self.assertEqual(saved_mixer[0].name, 'Coca cola')

        self.assertEqual(len(saved_mixer_ingredient), 1)
        self.assertEqual(saved_mixer_ingredient[0].mixer, saved_mixer[0])
        self.assertEqual(saved_mixer_ingredient[0].spirit, None)
        # TODO: add test for verbose name

        self.assertEqual(len(saved_spirit_ingredient), 1)
        self.assertEqual(saved_spirit_ingredient[0].spirit, saved_spirit[0])
        self.assertEqual(saved_spirit_ingredient[0].mixer, None)
        # TODO: add test for verbose name


class IngredientListViewTest(TestCase):

    def test_displays_all_items(self):
        Spirit.objects.create(name='Vodka', volume=39)
        Mixer.objects.create(name='Lemonade')

        response = self.client.get('/ingredients/')

        self.assertContains(response, 'Vodka')
        self.assertContains(response, 'Lemonade')


class NewSpiritTest(TestCase):

    def test_saving_a_POST_request(self):
        self.client.post(
            '/users/register/',
            data={'username': 'test_user', 'password': 'test_password'}
        )
        response = self.client.post(
            '/ingredients/spirit/create/',
            data={'name': 'Whiskey', 'volume': 40}
        )
        self.assertEqual(Spirit.objects.count(), 1)
        new_item = Spirit.objects.first()
        self.assertEqual(new_item.name, 'Whiskey')


    def test_redirects_after_POST(self):
        self.client.post(
            '/users/register/',
            data={'username': 'test_user', 'password': 'test_password'}
        )
        response = self.client.post(
            '/ingredients/spirit/create/',
            data={'name': 'Whiskey', 'volume': 40}
        )
        self.assertRedirects(response, '/ingredients/spirit/whiskey/')
