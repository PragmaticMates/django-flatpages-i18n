from modeltranslation.translator import translator, TranslationOptions

from flatpages_i18n.models import FlatPage_i18n, MenuItem


class FlatPageTranslationOptions(TranslationOptions):
    fields = ('url', 'title', 'content', )

translator.register(FlatPage_i18n, FlatPageTranslationOptions)


class MenuItemTranslationOptions(TranslationOptions):
    fields = ('title',)

translator.register(MenuItem, MenuItemTranslationOptions)
