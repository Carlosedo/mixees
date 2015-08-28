from django.test import TestCase
from django.core.urlresolvers import reverse

from .models import Cocktail


# Helper Methods
def add_cocktail(title, views):
    cocktail = Cocktail.objects.get_or_create(title=title)[0]
    cocktail.views = views
    cocktail.save()
    return cocktail


# Tests
class CocktailMethodTests(TestCase):
    def test_ensure_views_are_positive(self):
        """
        ensure_views_are_positive should results True for cocktails where views are zero or positive
        """
        cocktail = Cocktail(title='test',views=-1)
        cocktail.save()
        self.assertEqual((cocktail.views >= 0), True)


class ListViewTests(TestCase):
    def test_list_view_with_no_cocktails(self):
        """
        If no cocktails exist, an appropriate message should be displayed.
        """
        response = self.client.get(reverse('cocktail_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "There are no cocktails in the database.")
        self.assertQuerysetEqual(response.context['cocktail_list'], [])

    def test_index_view_with_categories(self):
        """
        If no cocktails exist, an appropriate message should be displayed.
        """
        add_cocktail('test',1)
        add_cocktail('temp',1)
        add_cocktail('tmp',1)
        add_cocktail('tmp test temp',1)

        response = self.client.get(reverse('cocktail_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "tmp test temp")

        num_cocktails = len(response.context['cocktail_list'])
        self.assertEqual(num_cocktails , 4)
