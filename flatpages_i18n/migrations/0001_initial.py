# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.management import call_command

from django.db import models, migrations
import mptt.fields
import django.utils.timezone


def sync_fields(apps, schema_editor):
    call_command(
        'sync_translation_fields',
        verbosity=1,
        interactive=False,
        run_syncdb=True,
    )
    call_command(
        'update_translation_fields',
        verbosity=1,
        interactive=False,
        run_syncdb=True,
    )


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FlatPage_i18n',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('machine_name', models.CharField(default=None, max_length=255, null=True, verbose_name='machine name', blank=True)),
                ('url', models.CharField(help_text="Example: '/about/contact/'. Make sure to have leading and trailing slashes.", max_length=100, verbose_name='URL', db_index=True)),
                ('title', models.CharField(max_length=200, verbose_name='title')),
                ('content', models.TextField(verbose_name='content', blank=True)),
                ('template_name', models.CharField(help_text="Example: 'flatpages_i18n/contact_page.html'. If this isn't provided, the system will use 'flatpages_i18n/default.html'.", max_length=70, verbose_name='template name', blank=True)),
                ('registration_required', models.BooleanField(default=False, help_text='If this is checked, only logged-in users will be able to view the page.', verbose_name='registration required')),
                ('weight', models.IntegerField(default=0, null=True, verbose_name='weight', blank=True, choices=[(-10, -10), (-9, -9), (-8, -8), (-7, -7), (-6, -6), (-5, -5), (-4, -4), (-3, -3), (-2, -2), (-1, -1), (0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9)])),
                ('created', models.DateTimeField(default=django.utils.timezone.now, verbose_name='created')),
                ('modified', models.DateTimeField(verbose_name='modified')),
                ('lft', models.PositiveIntegerField(editable=False, db_index=True)),
                ('rght', models.PositiveIntegerField(editable=False, db_index=True)),
                ('tree_id', models.PositiveIntegerField(editable=False, db_index=True)),
                ('level', models.PositiveIntegerField(editable=False, db_index=True)),
                ('parent', mptt.fields.TreeForeignKey(related_name='children', blank=True, to='flatpages_i18n.FlatPage_i18n', null=True)),
                ('sites', models.ManyToManyField(to='sites.Site')),
            ],
            options={
                'ordering': ('weight', 'created'),
                'verbose_name': 'flat page',
                'verbose_name_plural': 'flat pages',
            },
        ),
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('machine_name', models.CharField(default=None, max_length=255, null=True, verbose_name='machine name', blank=True)),
                ('custom_link', models.CharField(default=None, max_length=255, null=True, verbose_name='custom link', blank=True)),
                ('has_custom_link', models.BooleanField(default=False, verbose_name='has custom link')),
                ('title', models.CharField(default=None, max_length=255, null=True, verbose_name='title', blank=True)),
                ('weight', models.IntegerField(default=0, null=True, verbose_name='weight', blank=True, choices=[(-10, -10), (-9, -9), (-8, -8), (-7, -7), (-6, -6), (-5, -5), (-4, -4), (-3, -3), (-2, -2), (-1, -1), (0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9)])),
                ('created', models.DateTimeField(default=django.utils.timezone.now, verbose_name='created')),
                ('modified', models.DateTimeField(verbose_name='modified')),
                ('lft', models.PositiveIntegerField(editable=False, db_index=True)),
                ('rght', models.PositiveIntegerField(editable=False, db_index=True)),
                ('tree_id', models.PositiveIntegerField(editable=False, db_index=True)),
                ('level', models.PositiveIntegerField(editable=False, db_index=True)),
                ('flatpage', models.ForeignKey(default=None, blank=True, to='flatpages_i18n.FlatPage_i18n', null=True, verbose_name='flatpage')),
                ('parent', mptt.fields.TreeForeignKey(related_name='children', blank=True, to='flatpages_i18n.MenuItem', null=True)),
            ],
            options={
                'ordering': ('weight', 'created'),
                'verbose_name': 'menu item',
                'verbose_name_plural': 'menu items',
            },
        ),
        migrations.RunPython(sync_fields),
    ]
