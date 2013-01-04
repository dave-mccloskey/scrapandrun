# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'OutfitWearingProperties.photo'
        db.add_column('clothes_outfitwearingproperties', 'photo',
                      self.gf('django.db.models.fields.files.FileField')(max_length=300, null=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'OutfitWearingProperties.photo'
        db.delete_column('clothes_outfitwearingproperties', 'photo')


    models = {
        'clothes.accessorizedoutfit': {
            'Meta': {'object_name': 'AccessorizedOutfit'},
            'articles': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'accessorized_outfits'", 'blank': 'True', 'to': "orm['clothes.Article']"}),
            'base_outfit': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'accessorized_outfits'", 'to': "orm['clothes.Outfit']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'clothes.article': {
            'Meta': {'ordering': "['name']", 'object_name': 'Article'},
            'article_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'articles'", 'to': "orm['clothes.ArticleType']"}),
            'color': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'articles'", 'symmetrical': 'False', 'to': "orm['clothes.Color']"}),
            'cost': ('django.db.models.fields.DecimalField', [], {'max_digits': '6', 'decimal_places': '2'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'purchase_date': ('django.db.models.fields.DateField', [], {}),
            'purchase_location': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'articles'", 'on_delete': 'models.PROTECT', 'to': "orm['clothes.Store']"}),
            'size': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        'clothes.articletype': {
            'Meta': {'ordering': "['name']", 'object_name': 'ArticleType'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'clothes.color': {
            'Meta': {'ordering': "['basic_color', 'name']", 'object_name': 'Color'},
            'basic_color': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'clothes.date': {
            'Meta': {'ordering': "['date']", 'object_name': 'Date'},
            'date': ('django.db.models.fields.DateField', [], {'unique': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'outfits_worn': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'dates_worn'", 'symmetrical': 'False', 'through': "orm['clothes.OutfitWearingProperties']", 'to': "orm['clothes.AccessorizedOutfit']"})
        },
        'clothes.outfit': {
            'Meta': {'object_name': 'Outfit'},
            'articles': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'outfits'", 'symmetrical': 'False', 'to': "orm['clothes.Article']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'clothes.outfitwearingproperties': {
            'Meta': {'object_name': 'OutfitWearingProperties'},
            'accessorizedoutfit': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['clothes.AccessorizedOutfit']"}),
            'date': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['clothes.Date']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'photo': ('django.db.models.fields.files.FileField', [], {'max_length': '300', 'null': 'True'})
        },
        'clothes.store': {
            'Meta': {'ordering': "['name', 'location']", 'object_name': 'Store'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['clothes']