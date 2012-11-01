from django.contrib.sites.models import Site
from django.db import models
from django.utils.translation import ugettext_lazy as _


class FlatPage_i18n(models.Model):
    WEIGHT = [(i, i) for i in range(10)]

    url = models.CharField(_(u'URL'), max_length=100, db_index=True)
    title = models.CharField(_(u'title'), max_length=200)
    content = models.TextField(_(u'content'), blank=True)
    enable_comments = models.BooleanField(_(u'enable comments'))
    template_name = models.CharField(
        _(u'template name'), max_length=70, blank=True,
        help_text=_(u"Example: 'flatpages/contact_page.html'. If this isn't \
        provided, the system will use 'flatpages/default.html'."))
    registration_required = models.BooleanField(
        _(u'registration required'),
        help_text=_(u"If this is checked, only logged-in users will be able \
        to view the page."))
    weight = models.IntegerField(
        _(u'weight'), null=True, blank=True, default=0, choices=WEIGHT)
    sites = models.ManyToManyField(Site)

    def __unicode__(self):
        return u"%s -- %s" % (self.url, self.title)

    def get_absolute_url(self):
        return self.url

    class Meta:
        db_table = 'giaroo_flatpages'
        verbose_name = _(u'flat page')
        verbose_name_plural = _(u'flat pages')
        ordering = ('url', )
