from django.apps import apps
from django.test import TestCase
from story9.apps import Story9Config

class Story9ConfigTest(TestCase):
    def test_apps(self):
        self.assertEqual(Story9Config.name, 'story9')
        self.assertEqual(apps.get_app_config('story9').name, 'story9')
