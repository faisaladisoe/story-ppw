from django.apps import apps
from django.test import TestCase
from story8.apps import Story8Config

class Story6ConfigTest(TestCase):
    def test_apps(self):
        self.assertEqual(Story8Config.name, 'story8')
        self.assertEqual(apps.get_app_config('story8').name, 'story8')
