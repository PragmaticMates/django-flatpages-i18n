from django import forms
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

from flatpages_i18n.models import FlatPage_i18n


class FlatpageForm(forms.ModelForm):
    REQUIRED_MIDDLEWARE = 'django.middleware.common.CommonMiddleware'

    url = forms.RegexField(
        label=_(u'URL'), max_length=100, regex=r'^[-\w/\.~]+$',
        help_text=_(u"Example: '/about/contact/'. Make sure to have leading \
                    and trailing slashes."),
        error_message=_(u"This value must contain only letters, numbers, \
                          dots, underscores, dashes, slashes or tildes."))

    def clean_url(self):
        url = self.cleaned_data['url']

        if not url.startswith('/'):
            raise forms.ValidationError(_(u'URL is missing a leading slash.'))

        if settings.APPEND_SLASH and \
            self.REQUIRED_MIDDLEWARE in settings.MIDDLEWARE_CLASSES and \
                not url.endswith('/'):
            raise forms.ValidationError(_(u'URL is missing a trailing slash.'))

        return url

    def clean(self):
        url = self.cleaned_data.get('url', None)
        sites = self.cleaned_data.get('sites', None)
        same_url = FlatPage_i18n.objects.filter(url=url)

        if self.instance.pk:
            same_url = same_url.exclude(pk=self.instance.pk)

        if sites is None:
            raise forms.ValidationError(_(u'No sites selected!'))

        if same_url.filter(sites__in=sites).exists():
            for site in sites:
                if same_url.filter(sites=site).exists():
                    raise forms.ValidationError(
                        _(u'Flatpage with url %(url)s already exists \
                        for site %(site)s' % {'url': url, 'site': site}))

        return super(FlatpageForm, self).clean()

    class Meta:
        model = FlatPage_i18n
