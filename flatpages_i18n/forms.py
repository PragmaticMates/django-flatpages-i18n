from django import forms
from django.conf import settings
from django.core.validators import EMPTY_VALUES
from django.utils.translation import ugettext_lazy as _

from flatpages_i18n.models import FlatPage_i18n, MenuItem


class FlatpageForm(forms.ModelForm):
    REQUIRED_MIDDLEWARE = 'django.middleware.common.CommonMiddleware'

    def clean_url_value(self, url_key):
        url = self.cleaned_data.get(url_key, None)

        if url in EMPTY_VALUES:
            return

        # check leading slash
        if not url.startswith('/'):
            raise forms.ValidationError(_(u"URL '%(url)s' is missing a leading slash.") % {'url': url})

        # check trailing slash
        if settings.APPEND_SLASH and \
            self.REQUIRED_MIDDLEWARE in settings.MIDDLEWARE_CLASSES and \
                not url.endswith('/'):
            raise forms.ValidationError(_(u"URL '%(url)s' is missing a trailing slash.") % {'url': url})

        # check URL uniqueness
        sites = self.cleaned_data.get('sites', None)

        kwargs = {
            '{0}__{1}'.format(url_key, 'exact'): url,
        }
        same_url = FlatPage_i18n.objects.filter(**kwargs)

        if self.instance.pk:
            same_url = same_url.exclude(pk=self.instance.pk)

        if sites is None:
            raise forms.ValidationError(_(u'No sites selected!'))

        if same_url.filter(sites__in=sites).exists():
            for site in sites:
                if same_url.filter(sites=site).exists():
                    raise forms.ValidationError(_(u"Flatpage with URL '%(url)s' already exists \
                                                  for site %(site)s.") % {'url': url, 'site': site})
        return url

    def clean(self):
        for language in dict(settings.LANGUAGES).keys():
            url_key = 'url_%s' % language
            self.clean_url_value(url_key)
        return super(FlatpageForm, self).clean()

    class Meta:
        model = FlatPage_i18n



class MenuItemForm(forms.ModelForm):
    def clean_machine_name(self):
        machine_name = self.cleaned_data.get('machine_name', None)

        if machine_name in EMPTY_VALUES:
            return machine_name

        same_machine_name = MenuItem.objects.filter(machine_name=machine_name)

        if self.instance.pk:
            same_machine_name = same_machine_name.exclude(pk=self.instance.pk)

        if same_machine_name.exists():
            raise forms.ValidationError(
                _(u'Menu item with machine name %(machine_name)s already exists!' % {'machine_name': machine_name }))

        return machine_name

    class Meta:
        model = MenuItem


class ImageForm(forms.Form):
    file = forms.ImageField()


class FileForm(forms.Form):
    file = forms.FileField()
