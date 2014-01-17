# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'FlatPage_i18n'
        db.create_table('flatpages_i18n_flatpage_i18n', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('parent', self.gf('mptt.fields.TreeForeignKey')(blank=True, related_name='children', null=True, to=orm['flatpages_i18n.FlatPage_i18n'])),
            ('url', self.gf('django.db.models.fields.CharField')(max_length=100, db_index=True)),
            ('url_sk', self.gf('django.db.models.fields.CharField')(db_index=True, max_length=100, null=True, blank=True)),
            ('url_cs', self.gf('django.db.models.fields.CharField')(db_index=True, max_length=100, null=True, blank=True)),
            ('url_hu', self.gf('django.db.models.fields.CharField')(db_index=True, max_length=100, null=True, blank=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('title_sk', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('title_cs', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('title_hu', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('content', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('content_sk', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('content_cs', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('content_hu', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('template_name', self.gf('django.db.models.fields.CharField')(max_length=70, blank=True)),
            ('registration_required', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('weight', self.gf('django.db.models.fields.IntegerField')(default=0, null=True, blank=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')()),
            (u'lft', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            (u'rght', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            (u'tree_id', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            (u'level', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
        ))
        db.send_create_signal('flatpages_i18n', ['FlatPage_i18n'])

        # Adding M2M table for field sites on 'FlatPage_i18n'
        db.create_table('flatpages_i18n_flatpage_i18n_sites', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('flatpage_i18n', models.ForeignKey(orm['flatpages_i18n.flatpage_i18n'], null=False)),
            ('site', models.ForeignKey(orm['sites.site'], null=False))
        ))
        db.create_unique('flatpages_i18n_flatpage_i18n_sites', ['flatpage_i18n_id', 'site_id'])

        # Adding model 'MenuItem'
        db.create_table('flatpages_i18n_menuitem', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('parent', self.gf('mptt.fields.TreeForeignKey')(blank=True, related_name='children', null=True, to=orm['flatpages_i18n.MenuItem'])),
            ('flatpage', self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['flatpages_i18n.FlatPage_i18n'], null=True, blank=True)),
            ('custom_link', self.gf('django.db.models.fields.CharField')(default=None, max_length=255, null=True, blank=True)),
            ('has_custom_link', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('title_sk', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('title_cs', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('title_hu', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('weight', self.gf('django.db.models.fields.IntegerField')(default=0, null=True, blank=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')()),
            (u'lft', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            (u'rght', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            (u'tree_id', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            (u'level', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
        ))
        db.send_create_signal('flatpages_i18n', ['MenuItem'])

    def backwards(self, orm):
        # Deleting model 'FlatPage_i18n'
        db.delete_table('flatpages_i18n_flatpage_i18n')

        # Removing M2M table for field sites on 'FlatPage_i18n'
        db.delete_table('flatpages_i18n_flatpage_i18n_sites')

        # Deleting model 'MenuItem'
        db.delete_table('flatpages_i18n_menuitem')

    models = {
        'flatpages_i18n.flatpage_i18n': {
            'Meta': {'ordering': "('weight', 'created')", 'object_name': 'FlatPage_i18n'},
            'content': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'content_cs': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'content_hu': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'content_sk': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            u'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            u'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {}),
            'parent': ('mptt.fields.TreeForeignKey', [], {'blank': 'True', 'related_name': "'children'", 'null': 'True', 'to': "orm['flatpages_i18n.FlatPage_i18n']"}),
            'registration_required': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'sites': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['sites.Site']", 'symmetrical': 'False'}),
            'template_name': ('django.db.models.fields.CharField', [], {'max_length': '70', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'title_cs': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'title_hu': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'title_sk': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            u'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_index': 'True'}),
            'url_cs': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'url_hu': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'url_sk': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'weight': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'})
        },
        'flatpages_i18n.menuitem': {
            'Meta': {'ordering': "('weight', 'created')", 'object_name': 'MenuItem'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'custom_link': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'flatpage': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': "orm['flatpages_i18n.FlatPage_i18n']", 'null': 'True', 'blank': 'True'}),
            'has_custom_link': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            u'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            u'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {}),
            'parent': ('mptt.fields.TreeForeignKey', [], {'blank': 'True', 'related_name': "'children'", 'null': 'True', 'to': "orm['flatpages_i18n.MenuItem']"}),
            u'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'title_cs': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'title_hu': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'title_sk': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'weight': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'})
        },
        'sites.site': {
            'Meta': {'ordering': "('domain',)", 'object_name': 'Site', 'db_table': "'django_site'"},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['flatpages_i18n']