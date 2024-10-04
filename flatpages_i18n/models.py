from django.contrib.postgres.indexes import GinIndex
from django.contrib.sites.models import Site
from django.core.exceptions import ValidationError
from django.core.validators import EMPTY_VALUES
from django.db import models
from django.urls import reverse
from martor.models import MartorField
from modeltrans.fields import TranslationField
from mptt.models import MPTTModel, TreeForeignKey
from pragmatic.mixins import SlugMixin
from tinymce.models import HTMLField

from django.utils.translation import gettext_lazy as _


class FlatPage_i18n(SlugMixin, models.Model):
    FORCE_SLUG_REGENERATION = False

    title = models.CharField(_('title'), max_length=200)
    slug = models.SlugField(unique=True, max_length=SlugMixin.MAX_SLUG_LENGTH, blank=True, default='')
    machine_name = models.SlugField(_('machine name'), max_length=30, blank=True, help_text=_('unique'))
    content = HTMLField(_('content'), blank=True)
    template_name = models.CharField(
        _('template name'), max_length=70, blank=True,
        help_text=_(u"Example: 'flatpages_i18n/contact_page.html'. If this isn't provided, the system will use 'flatpages_i18n/default.html'."))
    registration_required = models.BooleanField(
        _('registration required'), default=False,
        help_text=_(u"If this is checked, only logged-in users will be able to view the page."))
    sites = models.ManyToManyField(Site)
    created = models.DateTimeField(_('created'), auto_now_add=True)
    modified = models.DateTimeField(_('modified'), auto_now=True)
    i18n = TranslationField(fields=('title', 'slug', 'content'))

    class Meta:
        verbose_name = _('flat page')
        verbose_name_plural = _('flat pages')
        ordering = ('title',)
        indexes = [GinIndex(fields=["i18n"]), ]
        constraints = [
            models.UniqueConstraint(
                fields=['machine_name'],
                condition=~models.Q(machine_name=''),
                name='unique_machine_name'
            )
        ]

    def __str__(self):
        return self.title_i18n

    def get_absolute_url(self):
        return reverse('flatpages_i18n:detail', args=(self.slug_i18n,))

    def clean(self):
        if self.slug not in EMPTY_VALUES:
            if self.__class__.objects.filter(slug=self.slug).exclude(pk=self.pk).exists():
                raise ValidationError(_("Slug %s is not unique") % self.slug)

        if self.machine_name not in EMPTY_VALUES:
            if self.__class__.objects.filter(machine_name=self.machine_name).exclude(pk=self.pk).exists():
                raise ValidationError(_("Machine name %s is not unique") % self.machine_name)

        return super().clean()


class Menu(models.Model):
    machine_name = models.SlugField(unique=True, max_length=50)

    class Meta:
        verbose_name = _('menu')
        verbose_name_plural = _('menus')

    def __str__(self):
        return self.machine_name


class MenuItem(MPTTModel):
    TARGETS = (
        ('_blank', _('Opens the linked document in a new window or tab')),
        ('_self', _('Opens the linked document in the same frame as it was clicked')),
        ('_parent', _('Opens the linked document in the parent frame')),
        ('_top', _('Opens the linked document in the full body of the window')),
    )

    menu = models.ForeignKey(Menu, verbose_name=_('menu'), on_delete=models.PROTECT, related_name='item_set')
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    flatpage = models.ForeignKey(FlatPage_i18n, verbose_name=_('flatpage'),
        null=True, blank=True, default=None, on_delete=models.SET_NULL)
    custom_link = models.CharField(_('custom link'), max_length=200, blank=True)
    target = models.CharField(_('target'), max_length=7, choices=TARGETS, default='_self')
    title = models.CharField(_('title'), max_length=100, blank=True)
    created = models.DateTimeField(_('created'), auto_now_add=True)
    modified = models.DateTimeField(_('modified'), auto_now=True)
    i18n = TranslationField(fields=('title', 'custom_link'))

    class MPTTMeta:
        order_insertion_by = ['title']

    class Meta:
        verbose_name = _('menu item')
        verbose_name_plural = _('menu items')
        indexes = [GinIndex(fields=["i18n"]), ]

    def __str__(self):
        if self.title_i18n not in EMPTY_VALUES:
            return self.title_i18n

        if self.flatpage:
            return str(self.flatpage)

        return str(self.pk)

    def get_absolute_url(self):
        if self.flatpage:
            return self.flatpage.get_absolute_url()

        return self.custom_link_i18n if self.custom_link_i18n else '#'
