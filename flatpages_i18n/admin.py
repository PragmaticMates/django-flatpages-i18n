from django.conf import settings
from django.contrib import admin
from django.db.models import TextField
from django.utils.translation import ugettext_lazy as _

from modeltranslation.admin import TranslationAdmin
from mptt.admin import MPTTModelAdmin

from forms import FlatpageForm, MenuItemForm
from models import FlatPage_i18n, MenuItem
from widgets import RedactorEditor


class FlatPageAdmin(MPTTModelAdmin, TranslationAdmin):
    form = FlatpageForm
    mptt_level_indent = 0

    fieldsets = (
        (None, {'fields': ('parent', 'machine_name', 'url', 'title', 'content', 'sites', )}),
        (_(u'Advanced options'), {
            'classes': ('collapse',),
            'fields': ('registration_required', 'template_name')
        })
    )
    list_display = ('indented_title', 'url', 'parent', 'weight')
    list_filter = ('sites', 'registration_required')
    list_editable = ['parent', 'weight']
    search_fields = ('url', 'title')
    readonly_fields = ('created', 'modified')

    class Media:
        js = ('js/flatpages_i18n/jquery.js', )
        css = {
            'all': ('css/flatpages_i18n/admin.css', )
        }

    def __init__(self, *args, **kwargs):
        if getattr(settings, 'FLATPAGES_EDITOR', None) == 'REDACTOR':
            self.formfield_overrides = {
                TextField: {'widget': RedactorEditor},
            }
        super(TranslationAdmin, self).__init__(*args, **kwargs)
        self._patch_list_editable()


    def indented_title(self, obj):
        level = getattr(obj, obj._mptt_meta.level_attr)

        if level is 0:
            return obj

        level_indicator = ''.join(['-' for i in range(level)])
        return '%s %s' % (level_indicator, unicode(obj))

admin.site.register(FlatPage_i18n, FlatPageAdmin)


class MenuItemAdmin(MPTTModelAdmin, TranslationAdmin):
    form = MenuItemForm
    mptt_level_indent = 0

    fields = ['parent', 'title', 'flatpage', 'machine_name', 'has_custom_link', 'custom_link', ]
    list_display = ('indented_title', 'machine_name', 'parent', 'weight')
    list_editable = ['parent', 'weight']

    def indented_title(self, obj):
        level = getattr(obj, obj._mptt_meta.level_attr)

        if level is 0:
            return obj

        level_indicator = ''.join(['-' for i in range(level)])
        return '%s %s' % (level_indicator, unicode(obj))

admin.site.register(MenuItem, MenuItemAdmin)
