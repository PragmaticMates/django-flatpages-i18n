from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from modeltranslation.admin import TranslationAdmin
from mptt.admin import MPTTModelAdmin

from forms import FlatpageForm
from models import FlatPage_i18n, MenuItem


class FlatPageAdmin(MPTTModelAdmin, TranslationAdmin):
    form = FlatpageForm
    #add_form = UserCreationForm
    mptt_level_indent = 0

    fieldsets = (
        (None, {'fields': ('parent', 'url', 'title', 'content', 'sites', )}),
        (_(u'Advanced options'), {
            'classes': ('collapse',),
            'fields': ('registration_required', 'template_name')
        })
    )
    list_display = ('indented_title', 'url', 'parent', 'weight')
    list_filter = ('sites', 'registration_required')
    list_editable = ['parent', 'weight']
    search_fields = ('url', 'title')

    def indented_title(self, obj):
        level = getattr(obj, obj._mptt_meta.level_attr)

        if level is 0:
            return obj

        level_indicator = ''.join(['-' for i in range(level)])
        return '%s %s' % (level_indicator, obj.title)

admin.site.register(FlatPage_i18n, FlatPageAdmin)


class MenuItemAdmin(MPTTModelAdmin, TranslationAdmin):
    mptt_level_indent = 0

    fields = ['parent', 'title', 'flatpage', 'has_custom_link', 'custom_link']
    list_display = ('indented_title', 'parent', 'weight')
    list_editable = ['parent', 'weight']

    def indented_title(self, obj):
        level = getattr(obj, obj._mptt_meta.level_attr)

        if level is 0:
            return obj

        level_indicator = ''.join(['-' for i in range(level)])
        return '%s %s' % (level_indicator, obj.title)

admin.site.register(MenuItem, MenuItemAdmin)
