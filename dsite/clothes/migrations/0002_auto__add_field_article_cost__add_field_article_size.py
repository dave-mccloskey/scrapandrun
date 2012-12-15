# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Article.cost'
        db.add_column('clothes_article', 'cost',
                      self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=6, decimal_places=2),
                      keep_default=False)

        # Adding field 'Article.size'
        db.add_column('clothes_article', 'size',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=30),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Article.cost'
        db.delete_column('clothes_article', 'cost')

        # Deleting field 'Article.size'
        db.delete_column('clothes_article', 'size')


    models = {
        'clothes.article': {
            'Meta': {'object_name': 'Article'},
            'article_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'articles'", 'to': "orm['clothes.ArticleType']"}),
            'color': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'articles'", 'symmetrical': 'False', 'to': "orm['clothes.Color']"}),
            'cost': ('django.db.models.fields.DecimalField', [], {'max_digits': '6', 'decimal_places': '2'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'purchase_date': ('django.db.models.fields.DateField', [], {}),
            'size': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        'clothes.articletype': {
            'Meta': {'object_name': 'ArticleType'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'clothes.color': {
            'Meta': {'object_name': 'Color'},
            'basic_color': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'clothes.date': {
            'Meta': {'object_name': 'Date'},
            'date': ('django.db.models.fields.DateField', [], {'unique': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'outfits_worn': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'dates'", 'symmetrical': 'False', 'to': "orm['clothes.Outfit']"})
        },
        'clothes.outfit': {
            'Meta': {'object_name': 'Outfit'},
            'articles': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'outfits'", 'symmetrical': 'False', 'to': "orm['clothes.Article']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['clothes']