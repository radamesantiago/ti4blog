# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Post.destaque'
        db.add_column(u'posts_post', 'destaque',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Post.destaque'
        db.delete_column(u'posts_post', 'destaque')


    models = {
        u'posts.post': {
            'Meta': {'object_name': 'Post'},
            'corpo': ('django.db.models.fields.TextField', [], {}),
            'data_criacao': ('django.db.models.fields.DateTimeField', [], {}),
            'destaque': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imagem': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'video': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        }
    }

    complete_apps = ['posts']