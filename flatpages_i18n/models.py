from django.contrib.sites.models import Site
from django.db import models
from django.utils.timezone import now
from django.utils.translation import ugettext_lazy as _

from mptt.models import MPTTModel, TreeForeignKey


class FlatPage_i18n(MPTTModel):
    WEIGHT = [(i, i) for i in range(-10, 10)]

    parent = TreeForeignKey(
        'self', null=True, blank=True, related_name='children')
    sites = models.ManyToManyField(Site)
    machine_name = models.CharField(_(u'machine name'), max_length=255,
        null=True, blank=True, default=None)
    url = models.CharField(_(u'URL'), max_length=100, db_index=True,
        help_text=_(u"Example: '/about/contact/'. Make sure to have leading and trailing slashes."))
    title = models.CharField(_(u'title'), max_length=200)
    content = models.TextField(_(u'content'), blank=True)
    template_name = models.CharField(
        _(u'template name'), max_length=70, blank=True,
        help_text=_(u"Example: 'flatpages_i18n/contact_page.html'. If this isn't \
        provided, the system will use 'flatpages_i18n/default.html'."))
    registration_required = models.BooleanField(
        _(u'registration required'), default=False,
        help_text=_(u"If this is checked, only logged-in users will be able \
        to view the page."))
    weight = models.IntegerField(
        _(u'weight'), null=True, blank=True, default=0, choices=WEIGHT)
    created = models.DateTimeField(_(u'created'), default=now)
    modified = models.DateTimeField(_(u'modified'))

    class MPTTMeta:
        order_insertion_by = ['weight']

    class Meta:
        verbose_name = _(u'flat page')
        verbose_name_plural = _(u'flat pages')
        ordering = ('weight', 'created')

    def __unicode__(self):
        return self.title

    def save(self, **kwargs):
        self.modified = now()
        super(FlatPage_i18n, self).save(**kwargs)

    def get_absolute_url(self):
        return self.url


class MenuItem(MPTTModel):
    WEIGHT = [(i, i) for i in range(-10, 10)]

    machine_name = models.CharField(_(u'machine name'), max_length=255,
        null=True, blank=True, default=None)
    parent = TreeForeignKey('self', related_name='children',
        null=True, blank=True)
    flatpage = models.ForeignKey(FlatPage_i18n, verbose_name=_('flatpage'),
        null=True, blank=True, default=None)
    custom_link = models.CharField(_(u'custom link'), max_length=255, null=True, blank=True, default=None)
    has_custom_link = models.BooleanField(_(u'has custom link'), default=False)
    title = models.CharField(_(u'title'), max_length=255,
        blank=True, null=True, default=None)
    weight = models.IntegerField(
        _(u'weight'), null=True, blank=True, default=0, choices=WEIGHT)
    created = models.DateTimeField(_(u'created'), default=now)
    modified = models.DateTimeField(_(u'modified'))

    class MPTTMeta:
        order_insertion_by = ['weight']

    class Meta:
        verbose_name = _(u'menu item')
        verbose_name_plural = _(u'menu items')
        ordering = ('weight', 'created')

    def __unicode__(self):
        if self.title and len(unicode(self.title).strip()) != 0:
            return self.title

        if self.flatpage:
            return unicode(self.flatpage)

        return unicode(self.pk)

    def save(self, **kwargs):
        self.modified = now()
        super(MenuItem, self).save(**kwargs)

    def get_link(self):
        if self.flatpage:
            return self.flatpage.url

        if self.has_custom_link:
            return self.custom_link

        return '#'
