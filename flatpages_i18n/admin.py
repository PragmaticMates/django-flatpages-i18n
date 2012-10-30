from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from modeltranslation.admin import TranslationAdmin

from flatpages_i18n.forms import FlatpageForm
from flatpages_i18n.models import FlatPage_i18n


class FlatPageAdmin(TranslationAdmin):
    #list_display = ('title',)
    #form = FlatpageForm
    fieldsets = (
        (None, {'fields': ('url', 'title', 'content', 'sites', )}),
        (_('Advanced options'), {'classes': ('collapse',), 'fields': ('enable_comments', 'registration_required', 'template_name')}),
        )
    #list_display = ('url', 'title', 'weight')
    list_display = ('url', 'title', )
    #list_editable = ('weight',)

    list_filter = ('sites', 'enable_comments', 'registration_required')
    search_fields = ('url', 'title')


admin.site.register(FlatPage_i18n, FlatPageAdmin)
