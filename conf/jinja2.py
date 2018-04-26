from django.contrib.staticfiles.storage import staticfiles_storage
from django.urls import reverse
from conf.settings import STATIC_URL, MEDIA_URL

from jinja2 import Environment


def environment(**options):
    env = Environment(**options)
    env.globals.update({
        'static': staticfiles_storage.url,
        'url': reverse,
        'STATIC_URL': STATIC_URL,
        'MEDIA_URL': MEDIA_URL,
        'BASE_TEMPLATE': 'base.html',
    })
    return env
