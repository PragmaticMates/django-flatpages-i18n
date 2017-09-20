from builtins import str as text
from django.contrib.sites.models import Site
from django.db import models
from django.utils import translation
from django.utils.six import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _
from mptt.models import MPTTModel, TreeForeignKey


@python_2_unicode_compatible
class FlatPage_i18n(MPTTModel):
    WEIGHT = [(i, i) for i in range(-10, 10)]

    parent = TreeForeignKey('self', related_name='children',
        null=True, blank=True)
    sites = models.ManyToManyField(Site)
    machine_name = models.CharField(_(u'machine name'), max_length=255,
        null=True, blank=True, default=None)
    url = models.CharField(_(u'URL'), max_length=100, db_index=True,
        help_text=_(u"Example: '/about/contact/'. Make sure to have leading and trailing slashes."))
    title = models.CharField(_(u'title'), max_length=200)
    content = models.TextField(_(u'content'), blank=True)
    template_name = models.CharField(
        _(u'template name'), max_length=70, blank=True,
        help_text=_(u"Example: 'flatpages_i18n/contact_page.html'. If this isn't provided, "
                    u"the system will use settings.FLATPAGES_DEFAULT_TEMPLATE or 'flatpages_i18n/default.html'."))
    registration_required = models.BooleanField(
        _(u'registration required'), default=False,
        help_text=_(u"If this is checked, only logged-in users will be able to view the page."))
    weight = models.IntegerField(
        _(u'weight'), null=True, blank=True, default=0, choices=WEIGHT)
    created = models.DateTimeField(_(u'created'), auto_now_add=True)
    modified = models.DateTimeField(_(u'modified'), auto_now=True)

    class MPTTMeta:
        order_insertion_by = ['weight']

    class Meta:
        verbose_name = _(u'flat page')
        verbose_name_plural = _(u'flat pages')
        ordering = ('weight', 'created')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        language = translation.get_language()
        return '/{}{}'.format(language, self.url)


@python_2_unicode_compatible
class MenuItem(MPTTModel):
    WEIGHT = [(i, i) for i in range(-10, 10)]
    TARGETS = (
        ('_blank', _('Opens the linked document in a new window or tab')),
        ('_self', _('Opens the linked document in the same frame as it was clicked')),
        ('_parent', _('Opens the linked document in the parent frame')),
        ('_top', _('Opens the linked document in the full body of the window')),
    )

    machine_name = models.CharField(_(u'machine name'), max_length=255,
        null=True, blank=True, default=None)
    parent = TreeForeignKey('self', related_name='children',
        null=True, blank=True)
    flatpage = models.ForeignKey(FlatPage_i18n, verbose_name=_('flatpage'),
        null=True, blank=True, default=None)
    custom_link = models.CharField(_(u'custom link'), max_length=255,
        null=True, blank=True, default=None)
    has_custom_link = models.BooleanField(_(u'has custom link'), default=False)
    target = models.CharField(_(u'target'), max_length=7, choices=TARGETS, default='_self')
    title = models.CharField(_(u'title'), max_length=255,
        blank=True, null=True, default=None)
    weight = models.IntegerField(_(u'weight'), choices=WEIGHT,
        null=True, blank=True, default=0)
    created = models.DateTimeField(_(u'created'), auto_now_add=True)
    modified = models.DateTimeField(_(u'modified'), auto_now=True)

    class MPTTMeta:
        order_insertion_by = ['weight']

    class Meta:
        verbose_name = _(u'menu item')
        verbose_name_plural = _(u'menu items')
        ordering = ('weight', 'created')

    def __str__(self):
        if self.title and len(text(self.title).strip()) != 0:
            return self.title

        if self.flatpage:
            return text(self.flatpage)

        return text(self.pk)

    def get_link(self):
        if self.flatpage:
            return self.flatpage.get_absolute_url()

        if self.has_custom_link:
            return self.custom_link

        return '#'
