from django.utils.translation import ugettext_lazy as _

SEASON_CHOICES = (
    ('зима', _('Зима')),
    ('весна', _('Весна')),
    ('лето', _('Лето')),
    ('осень', _('Осень')),
)
KGS = 'KGS'
RUB = 'RUB'
CURRENCY_CHOICES = (
    (KGS, _('сом')),
    (RUB, _('рубль'))
)
