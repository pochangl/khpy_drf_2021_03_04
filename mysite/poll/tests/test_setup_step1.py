from django.conf import settings
from django.test import TestCase


class TestSetup(TestCase):
    def test_apps(self):
        assert 'poll' in settings.INSTALLED_APPS, 'mysite/settings.py 的 INSTALLED_APP 裡沒有 poll package'
