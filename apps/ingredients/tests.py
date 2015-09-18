from django.test import TestCase

from .models import Liquid, Spirit, Mixer, Ingredient


class LiquidsModelTest(TestCase):

    def test_saving_and_retrieving_items(self):
        spirit = Spirit()
        spirit.name = 'Ron Brugal'
        spirit.volume = 40
        spirit.save()

        mixer = Mixer()
        mixer.name = 'Coca cola'
        mixer.save()

        saved_spirit = Spirit.objects.all()
        saved_mixer = Mixer.objects.all()

        self.assertEqual(len(saved_spirit), 1)
        self.assertEqual(saved_spirit[0].name, 'Ron Brugal')
        self.assertEqual(saved_spirit[0].volume, 40)

        self.assertEqual(len(saved_mixer), 1)
        self.assertEqual(saved_mixer[0].name, 'Coca cola')

class IngredientListViewTest(TestCase):

    def test_displays_all_items(self):
        Spirit.objects.create(name='Vodka', volume=39)
        Mixer.objects.create(name='Lemonade')

        response = self.client.get('/ingredients/')

        self.assertContains(response, 'Vodka')
        self.assertContains(response, 'Lemonade')
