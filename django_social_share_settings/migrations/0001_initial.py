# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'SocialShareSettings'
        db.create_table(u'django_social_share_settings_socialsharesettings', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('site', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sites.Site'], null=True, blank=True)),
            ('track_social_share_clicks', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal(u'django_social_share_settings', ['SocialShareSettings'])

        # Adding model 'SocialShareLink'
        db.create_table(u'django_social_share_settings_socialsharelink', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['django_social_share_settings.SocialShareSettings'])),
            ('order', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('to_template', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('title_template', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('description_template', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'django_social_share_settings', ['SocialShareLink'])


    def backwards(self, orm):
        # Deleting model 'SocialShareSettings'
        db.delete_table(u'django_social_share_settings_socialsharesettings')

        # Deleting model 'SocialShareLink'
        db.delete_table(u'django_social_share_settings_socialsharelink')


    models = {
        u'django_social_share_settings.socialsharelink': {
            'Meta': {'object_name': 'SocialShareLink'},
            'description_template': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['django_social_share_settings.SocialShareSettings']"}),
            'title_template': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'to_template': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        u'django_social_share_settings.socialsharesettings': {
            'Meta': {'object_name': 'SocialShareSettings'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sites.Site']", 'null': 'True', 'blank': 'True'}),
            'track_social_share_clicks': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        },
        u'sites.site': {
            'Meta': {'ordering': "(u'domain',)", 'object_name': 'Site', 'db_table': "u'django_site'"},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['django_social_share_settings']