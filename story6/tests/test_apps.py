from django.apps import apps
from django.test import TestCase
from story6.apps import Story6Config

class Story6ConfigTest(TestCase):
    def test_apps(self):
        self.assertEqual(Story6Config.name, 'story6')
        self.assertEqual(apps.get_app_config('story6').name, 'story6')
