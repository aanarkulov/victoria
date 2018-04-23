from django.db import models
from django.utils.translation import ugettext_lazy as _
from geoposition.fields import GeopositionField
from ckeditor.fields import RichTextField


class Banner(models.Model):
    title = models.CharField(_('Заголовок'), max_length=255, blank=True)
    description = RichTextField(_('Описание'), blank=True)
    image = models.ImageField(_('Картинка'), upload_to='images/jpg')

    class Meta:
        verbose_name = _('Банер')
        verbose_name_plural = _('Банер')


class Feedback(models.Model):
    name = models.CharField(_('Имя'), max_length=255)
    phone = models.CharField(_('Телефон'), max_length=255)
    email = models.EmailField(_('Эл. почта'), max_length=255)
    message = models.TextField(_('Сообщение'), null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Обратная связь')
        verbose_name_plural = _('Обратные связи')


class ContactNumber(models.Model):
    phone = models.CharField(_('Номер'), max_length=255)

    def __str__(self):
        return self.phone

    class Meta:
        verbose_name = _('Контактный номер')
        verbose_name_plural = _('Контактные номера')


class Advantage(models.Model):
    title = models.CharField(_('Заголовок'), max_length=255)
    description = RichTextField(_('Описание'))
    icon = models.ImageField(_('Икона'), upload_to='images/png')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Преимущество')
        verbose_name_plural = _('Преимуществa')


class About(models.Model):
    title = models.CharField(_('Заголовок'), max_length=255)
    description = RichTextField(_('Описание'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('О Виктории')
        verbose_name_plural = _('О Виктории')


class Review(models.Model):
    city = models.CharField(_('Город'), max_length=255)
    full_name = models.CharField(_('Полное имя'), max_length=255)
    text = RichTextField(_('Текст'))
    image = models.ImageField(_('Фото'), upload_to='images/png')

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = _('Отзыв')
        verbose_name_plural = _('Отзывы')


class LinkToSocialNetwork(models.Model):
    facebook = models.URLField(_('Facebook'), default='https://www.facebook.com')
    instagram = models.URLField(_('Instagram'), default='https://www.instagram.com')
    vk = models.URLField(_('VKontacte'), default='https://vk.com')

    class Meta:
        verbose_name = _('Ссылка на соц сеть')
        verbose_name_plural = _('Ссылки на соц сети')


class PaymentAndDelivery(models.Model):
    title = models.CharField(_('Заголовок'), max_length=255)
    slug = models.SlugField(_('Слаг'), max_length=255)
    description = RichTextField(_('Описание'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Оплата и Доставка')
        verbose_name_plural = _('Оплата и Доставка')


class WeCooperate(models.Model):
    title = models.CharField(_('Заголовок'), max_length=255)
    description = RichTextField(_('Описание'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Мы сотрудничаем')
        verbose_name_plural = _('Мы сотрудничаем')


class Partner(models.Model):
    title = models.CharField(_('Нвзвание Партнера'), max_length=255)
    url = models.URLField(_('Ссылка на сайт партнера'), blank=True)
    logo = models.ImageField(_('Логотип'), upload_to='images/png')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Партнер')
        verbose_name_plural = _('Партнеры')


class Contact(models.Model):
    address = models.TextField(_('Адрес'), null=True)
    phone = models.CharField(_('Телефон'), max_length=255, null=True)
    email = models.EmailField(_('Эл. почта'), null=True)
    operating_mode = models.CharField(_('Режим работы'), max_length=255, null=True)

    class Meta:
        verbose_name = _('Контакт')
        verbose_name_plural = _('Контакты')


class Coordinate(models.Model):
    address = models.CharField(_('Адрес'), max_length=255)
    position = GeopositionField(_('Координаты'))

    def __str__(self):
        return self.address

    class Meta:
        verbose_name = _("Координат")
        verbose_name_plural = _("Координаты")
