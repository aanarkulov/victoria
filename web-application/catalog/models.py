from colorfield.fields import ColorField
from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext_lazy as _
from ckeditor.fields import RichTextField

from catalog.choices import SEASON_CHOICES, CURRENCY_CHOICES, KGS


class CategoryType(models.Model):
    title = models.CharField(_('Заголовок'), max_length=255)
    slug = models.SlugField(_('Слаг'), max_length=255, unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Категория Тип')
        verbose_name_plural = _('Категория Типы')


class CategorySize(models.Model):
    size = models.CharField(_('Размер'), max_length=255)
    slug = models.SlugField(_('Слаг'), max_length=255, unique=True)

    def __str__(self):
        return self.size

    class Meta:
        verbose_name = _('Категория Размер')
        verbose_name_plural = _('Категория Размеры')


class CategorySeason(models.Model):
    season = models.CharField(_('Сезон'), max_length=255, unique=True, choices=SEASON_CHOICES)
    image = models.ImageField(_('Картинка'), upload_to='images/jpg')

    def __str__(self):
        return self.season

    class Meta:
        verbose_name = _('Категория Сезон')
        verbose_name_plural = _('Категория Сезоны')


class ProductColors(models.Model):
    name = models.CharField(_('Название цвета'), max_length=255)
    color = ColorField(_('Цвет'), default='#ffff00')

    class Meta:
        verbose_name = _('Цвет товара')
        verbose_name_plural = _('Цвета товара')

    def __str__(self):
        return self.name


class Product(models.Model):
    type = models.ManyToManyField(CategoryType, verbose_name=_('Категория Тип'))
    size = models.ManyToManyField(CategorySize, verbose_name=_('Категория Рамер'))
    season = models.ManyToManyField(CategorySeason, default='', verbose_name=_('Категория Сезон'))
    color = models.ManyToManyField(ProductColors, related_name='product_colors', verbose_name=_('Категория Цвет'))
    name = models.CharField(_('Название'), max_length=255)
    slug = models.SlugField(_('Слаг'), max_length=50, unique=True)
    description = RichTextField(_('Описание'), null=True)
    amount = models.DecimalField(_('Цена'), max_digits=10, decimal_places=2)
    currency = models.CharField(_('Валюта'), max_length=255, default=KGS, choices=CURRENCY_CHOICES)
    fabric_structure = models.CharField(_('Состав ткани'), max_length=255, null=True, blank=True)
    weight_of_1_line = models.CharField(_('Вес 1 линии'), max_length=255, null=True, blank=True)
    in_the_1st_line = models.CharField(_('В 1-ой линейке'), max_length=255, null=True, blank=True)
    action = models.BooleanField(_('Акция'), default=False,
                                 help_text=_('Поставьте галочку, если едет акция на этот товар'))
    popular = models.BooleanField(_('Популярное'), default=False, help_text=_('Поставьте галочку, если товар популярный'))
    added_to = models.DateTimeField(_('Создано'), auto_now_add=True)
    updated = models.DateTimeField(_('Обновлено'), auto_now=True)
    create_at = models.ForeignKey(User, related_name='user_products')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Товар')
        verbose_name_plural = _('Товары')


class ProductImages(models.Model):
    product = models.ForeignKey(Product, verbose_name=_('Товар'), related_name='product_images')
    image = models.ImageField(_('Картинкa'), upload_to='images/png')

    class Meta:
        verbose_name = _('Картинка Товара')
        verbose_name_plural = _('Картинки Товара')


# class Descriptions(models.Model):
#     description = models.TextField(verbose_name=_('Описание'))
#
#     class Meta:
#         verbose_name = _('Описание')
#         verbose_name_plural = _('Описании')
#
#     def __str__(self):
#         return self.description


class AboutOurTrousers(models.Model):
    title = models.CharField(_('Заголовок'), max_length=255)
    description = RichTextField(_('Описание'))
    description2 = RichTextField(_('Описание'), blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('О наших брюках')
        verbose_name_plural = _('О наших брюках')


class OrderOfProduct(models.Model):
    name = models.CharField(_('Имя'), max_length=255)
    phone = models.CharField(_('Телефон'), max_length=255)
    email = models.EmailField(_('Эл. почта'), max_length=255)
    id_product = models.CharField(_('ID товара'), max_length=255)
    color = models.ForeignKey(ProductColors, verbose_name=_('Цвет товара'))
    quantity = models.PositiveIntegerField(_('Количество'), default=1)
    total_amount = models.DecimalField(_('Итого'), max_digits=20, decimal_places=2)
    date_created = models.DateTimeField(_('Время заказа'), auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Заказ')
        verbose_name_plural = _('Заказы')
