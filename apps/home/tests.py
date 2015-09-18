from django.core.urlresolvers import resolve, reverse
from django.test import TestCase
from django.template.loader import render_to_string

from apps.home.views import IndexView


class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.view_name, 'homepage')


    def test_home_page_returns_correct_html(self):
        response = self.client.get(reverse('homepage'))
        expected_html = render_to_string(
            'home/index.html',
            {
                'visits': '1',
                'request': {'path': '/'}
            }
        )
        self.assertEqual(response.content.decode(), expected_html)
