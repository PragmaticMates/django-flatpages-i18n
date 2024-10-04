# Generated by Django 5.0.9 on 2024-10-04 20:03

import tinymce.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flatpages_i18n', '0004_markdown_to_html'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flatpage_i18n',
            name='content',
            field=tinymce.models.HTMLField(blank=True, verbose_name='content'),
        ),
    ]
