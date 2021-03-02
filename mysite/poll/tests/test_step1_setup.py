from os import path
from django.conf import settings
from django.test import TestCase


class TestSetup(TestCase):
    def test_apps(self):
        assert 'poll' in settings.INSTALLED_APPS, 'mysite/settings.py 的 INSTALLED_APP 裡沒有 poll package'

    def test_model_file(self):
        assert path.exists('poll/models.py'), 'poll/models.py 沒有定義'

    def test_migration_file(self):
        assert path.exists('poll/migrations/0001_initial.py'), '還沒有跑 python manage.py makemigrations poll'
