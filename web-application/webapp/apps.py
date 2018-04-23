from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class WebappConfig(AppConfig):
    name = 'webapp'
    verbose_name = _('Веб приложение')
