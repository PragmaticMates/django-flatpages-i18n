from django.conf import settings
from django.db import migrations, models
from martor.templatetags.martortags import safe_markdown
from flatpages_i18n.models import FlatPage_i18n


def markdown_to_html(apps, schema_editor):
    # class from get_model() does not support _i18n or _<language> attributes
    # FlatPage_i18n = apps.get_model('flatpages_i18n', 'FlatPage_i18n')

    flatpages = FlatPage_i18n.objects.all()

    languages = dict(settings.LANGUAGES).keys()

    attrs = ['content_%s' % lang for lang in languages]

    for flatpage in flatpages:
        for attr in attrs:
            _migrate_content(flatpage, attr)

        flatpage.save()

    # can't use bulk_update because attr is not concrete field
    # FlatPage_i18n.objects.bulk_update(flatpages, fields=attrs)


def _migrate_content(flatpage, attr):
    content_martor = getattr(flatpage, attr, '')
    content_html = safe_markdown(content_martor) if content_martor else content_martor

    if content_html is not None:
        setattr(flatpage, attr, content_html)


class Migration(migrations.Migration):

    dependencies = [
        ('flatpages_i18n', '0003_auto_20220714_1614'),
    ]

    operations = [
        migrations.RunPython(markdown_to_html),
    ]
