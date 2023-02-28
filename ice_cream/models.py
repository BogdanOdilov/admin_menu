from django.core.cache import cache
from django.db import models

from settings import MYMENU_CACHE_KEY


class Menu(models.Model):
    "Site menu entity"

    name = models.CharField(
        max_length=255)
    slug = models.SlugField(
        max_length=200,
        unique=True)

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        cached_menus = cache.get(MYMENU_CACHE_KEY)
        if cached_menus is not None:
            cache.delete(MYMENU_CACHE_KEY)
        super(Menu, self).save(*args, **kwargs)

    def items(self):
        return self.menuitem_set.all()


class MenuItem(models.Model):
    "Site menu items"

    LINK_TARGET_CHOICES = (
        ('_blank', '_blank'),
        ('_top', '_top'),
        ('_parent', '_parent'),
    )

    name = models.CharField(
        max_length=255)
    url = models.CharField(
        max_length=255)
    title = models.CharField(
        max_length=255, 
        blank=True,
        null=True)
    target = models.CharField(
        max_length=10,
        choices=LINK_TARGET_CHOICES,
        null=True,
        blank=True
    )
    menu = models.ForeignKey('Menu')

    def save(self, *args, **kwargs):
        cached_menus = cache.get(MYMENU_CACHE_KEY)
        if cached_menus is not None:
            cache.delete(MYMENU_CACHE_KEY)
        super(MenuItem, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.url

class TreeMenuCategory(models.Model):

    LABELS = {
        'name': 'Name',
        'verbose_name': 'Verbose name'
    }

    class Meta:
        verbose_name = 'Menu category'
        verbose_name_plural = 'Menu categories'

    name = models.CharField(
        LABELS['name'],
        max_length=255,
        blank=True,
        null=False)
    verbose_name = models.CharField(
        LABELS['verbose_name'],
        max_length=255,
        blank=True,
        null=False)

    def __str__(self):
        return self.verbose_name


class TreeMenu(models.Model):

    LABELS = {
        'name': 'Name',
        'category': 'Category',
        'path': 'Link',
        'parent': 'Parent element'
    }

    class Meta:
        verbose_name = 'Menu item'
        verbose_name_plural = 'Menu items'

    name = models.CharField(
        LABELS['name'],
        max_length=255,
        blank=True,
        null=False)

    category = models.ForeignKey(
        TreeMenuCategory,
        verbose_name=LABELS['category'],
        on_delete=models.CASCADE,
        blank=False,
        null=False
    )
    path = models.CharField(
        LABELS['path'],
        max_length=1000,
        blank=True,
        null=False)

    parent = models.ForeignKey(
        'self',
        verbose_name=LABELS['parent'],
        on_delete=models.SET_DEFAULT,
        null=True,
        blank=True,
        default=0
    )

    def __str__(self):
        return self.name
