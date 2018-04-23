import threading

from django.core.mail import EmailMessage
from django.db import models

from django.template.loader import render_to_string
from django.utils.translation import ugettext_lazy as _
from ckeditor.fields import RichTextField


class Type(models.Model):
    title = models.CharField(_('Заголовок'), max_length=255)
    slug = models.SlugField(_('Слаг'), max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Тип')
        verbose_name_plural = _('Типы')


class News(models.Model):
    type = models.ForeignKey(Type, verbose_name=_('Тип'))
    title = models.CharField(_('Заголовок'), max_length=255)
    slug = models.SlugField(_('Слаг'), max_length=255, unique=True)
    description = RichTextField(_('Описание'))
    description2 = RichTextField(_('Описание 2'), blank=True)
    image = models.ImageField(_('Картинка'), upload_to='images/jpg')
    send_to_subscribers = models.BooleanField(_('Отправить подписчикам'), default=False)
    pub_date = models.DateTimeField(_('Дата публакации'), auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Новость')
        verbose_name_plural = _('Новости')

    def save(self, *args, **kwargs):
        super(News, self).save(*args, **kwargs)

        if self.send_to_subscribers == True:
            thread = threading.Thread(target=self.send_news_to_subscribers,
                                      args=(self.type, self.title, self.description))
            thread.start()

    @staticmethod
    def send_news_to_subscribers(type, title, description):
        _subscribers = Subscriber.objects.all()
        subscribers = []
        for subscriber in _subscribers:
            subscribers.append(subscriber)
        context = {
            'title': title,
            'description': description,
        }

        content = render_to_string('send_mail/news_to_subscribers.html', context)
        mail = EmailMessage(_('{0} от victoria.kg'.format(type)), content, to=subscribers)
        mail.content_subtype = 'html'
        mail.send()


class Subscriber(models.Model):
    email = models.EmailField(_('Эл. почта'), max_length=255)

    class Meta:
        verbose_name = _('Подписчик')
        verbose_name_plural = _('Подписчики')

    def __str__(self):
        return self.email
