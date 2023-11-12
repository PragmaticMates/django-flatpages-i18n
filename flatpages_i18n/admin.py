from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from modeltrans.admin import ActiveLanguageMixin
from mptt.admin import DraggableMPTTAdmin

from flatpages_i18n.models import FlatPage_i18n, MenuItem, Menu


@admin.register(FlatPage_i18n)
class FlatPageAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {'fields': ('title_i18n', 'slug_i18n', 'machine_name', 'content_i18n', 'sites', )}),
        (_(u'Advanced options'), {
            'classes': ('collapse',),
            'fields': ('registration_required', 'template_name')
        })
    )
    list_display = ('title_i18n', 'slug_i18n', 'machine_name')
    list_filter = ('sites', 'registration_required')
    search_fields = ('slug_i18n', 'title_i18n', 'content_i18n', 'machine_name')
    readonly_fields = ('created', 'modified')


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('machine_name',)
    list_display_links = ('machine_name',)


@admin.register(MenuItem)
class MenuItemAdmin(ActiveLanguageMixin, DraggableMPTTAdmin):
    search_fields = ('title_i18n', 'custom_link_i18n')
    list_select_related = ['flatpage', 'menu']
    list_display = ('tree_actions', 'indented_title', 'menu', 'title_i18n', 'custom_link_i18n', 'flatpage', 'url')
    list_display_links = ('indented_title',)
    list_editable = ['menu', 'flatpage', 'title_i18n', 'custom_link_i18n']
    list_filter = ['menu']
    # fields = ['menu', 'title_i18n', 'flatpage', 'custom_link_i18n', 'target']

    def url(self, obj):
        return obj.get_absolute_url()
