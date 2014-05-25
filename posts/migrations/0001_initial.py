# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Post'
        db.create_table('posts_post', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('titulo', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('corpo', self.gf('django.db.models.fields.TextField')()),
            ('data_criacao', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal('posts', ['Post'])


    def backwards(self, orm):
        # Deleting model 'Post'
        db.delete_table('posts_post')


    models = {
        'posts.post': {
            'Meta': {'object_name': 'Post'},
            'corpo': ('django.db.models.fields.TextField', [], {}),
            'data_criacao': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['posts']