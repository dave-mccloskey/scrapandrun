# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Store'
        db.create_table('clothes_store', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('location', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('clothes', ['Store'])

        # Adding model 'Color'
        db.create_table('clothes_color', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('basic_color', self.gf('django.db.models.fields.CharField')(max_length=2)),
        ))
        db.send_create_signal('clothes', ['Color'])

        # Adding model 'ArticleType'
        db.create_table('clothes_articletype', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('clothes', ['ArticleType'])

        # Adding model 'Article'
        db.create_table('clothes_article', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('purchase_date', self.gf('django.db.models.fields.DateField')()),
            ('article_type', self.gf('django.db.models.fields.related.ForeignKey')(related_name='articles', to=orm['clothes.ArticleType'])),
            ('cost', self.gf('django.db.models.fields.DecimalField')(max_digits=6, decimal_places=2)),
            ('size', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('purchase_location', self.gf('django.db.models.fields.related.ForeignKey')(related_name='articles', on_delete=models.PROTECT, to=orm['clothes.Store'])),
        ))
        db.send_create_signal('clothes', ['Article'])

        # Adding M2M table for field color on 'Article'
        db.create_table('clothes_article_color', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('article', models.ForeignKey(orm['clothes.article'], null=False)),
            ('color', models.ForeignKey(orm['clothes.color'], null=False))
        ))
        db.create_unique('clothes_article_color', ['article_id', 'color_id'])

        # Adding model 'Outfit'
        db.create_table('clothes_outfit', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('clothes', ['Outfit'])

        # Adding M2M table for field articles on 'Outfit'
        db.create_table('clothes_outfit_articles', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('outfit', models.ForeignKey(orm['clothes.outfit'], null=False)),
            ('article', models.ForeignKey(orm['clothes.article'], null=False))
        ))
        db.create_unique('clothes_outfit_articles', ['outfit_id', 'article_id'])

        # Adding model 'AccessorizedOutfit'
        db.create_table('clothes_accessorizedoutfit', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('base_outfit', self.gf('django.db.models.fields.related.ForeignKey')(related_name='accessorized_outfits', to=orm['clothes.Outfit'])),
        ))
        db.send_create_signal('clothes', ['AccessorizedOutfit'])

        # Adding M2M table for field articles on 'AccessorizedOutfit'
        db.create_table('clothes_accessorizedoutfit_articles', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('accessorizedoutfit', models.ForeignKey(orm['clothes.accessorizedoutfit'], null=False)),
            ('article', models.ForeignKey(orm['clothes.article'], null=False))
        ))
        db.create_unique('clothes_accessorizedoutfit_articles', ['accessorizedoutfit_id', 'article_id'])

        # Adding model 'Date'
        db.create_table('clothes_date', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date', self.gf('django.db.models.fields.DateField')(unique=True)),
        ))
        db.send_create_signal('clothes', ['Date'])

        # Adding M2M table for field outfits_worn on 'Date'
        db.create_table('clothes_date_outfits_worn', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('date', models.ForeignKey(orm['clothes.date'], null=False)),
            ('accessorizedoutfit', models.ForeignKey(orm['clothes.accessorizedoutfit'], null=False))
        ))
        db.create_unique('clothes_date_outfits_worn', ['date_id', 'accessorizedoutfit_id'])


    def backwards(self, orm):
        # Deleting model 'Store'
        db.delete_table('clothes_store')

        # Deleting model 'Color'
        db.delete_table('clothes_color')

        # Deleting model 'ArticleType'
        db.delete_table('clothes_articletype')

        # Deleting model 'Article'
        db.delete_table('clothes_article')

        # Removing M2M table for field color on 'Article'
        db.delete_table('clothes_article_color')

        # Deleting model 'Outfit'
        db.delete_table('clothes_outfit')

        # Removing M2M table for field articles on 'Outfit'
        db.delete_table('clothes_outfit_articles')

        # Deleting model 'AccessorizedOutfit'
        db.delete_table('clothes_accessorizedoutfit')

        # Removing M2M table for field articles on 'AccessorizedOutfit'
        db.delete_table('clothes_accessorizedoutfit_articles')

        # Deleting model 'Date'
        db.delete_table('clothes_date')

        # Removing M2M table for field outfits_worn on 'Date'
        db.delete_table('clothes_date_outfits_worn')


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
            'outfits_worn': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'dates_worn'", 'symmetrical': 'False', 'to': "orm['clothes.AccessorizedOutfit']"})
        },
        'clothes.outfit': {
            'Meta': {'object_name': 'Outfit'},
            'articles': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'outfits'", 'symmetrical': 'False', 'to': "orm['clothes.Article']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'clothes.store': {
            'Meta': {'ordering': "['name', 'location']", 'object_name': 'Store'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['clothes']