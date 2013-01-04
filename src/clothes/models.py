from picasa import PicasaField

from django.db import models
from django.db.models import Sum, Q, F
from django.core.exceptions import ValidationError

import datetime
from itertools import chain, ifilterfalse

class Store(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=100)

    class Meta:
        ordering = ['name', 'location']

    def __unicode__(self):
        return self.name + ' (' + self.location + ')'


class Color(models.Model):
    BASIC_COLORS = (
        (u'RD', u'Red'),
        (u'PK', u'Pink'),
        (u'OR', u'Orange'),
        (u'YL', u'Yellow'),
        (u'GR', u'Green'),
        (u'TK', u'Turquoise'),
        (u'BL', u'Blue'),
        (u'IN', u'Indigo'),
        (u'VI', u'Violet'),
        (u'BK', u'Black'),
        (u'WH', u'White'),
        (u'NU', u'Neutral'),
    )

    name = models.CharField(max_length=200)
    basic_color = models.CharField(max_length=2, choices=BASIC_COLORS)

    class Meta:
        ordering = ['basic_color', 'name']

    def __unicode__(self):
        return self.name + " (" + self.get_basic_color_display() + ")"


class ArticleType(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        ordering = ['name']

    def __unicode__(self):
        return self.name


class Article(models.Model):
    name = models.CharField(max_length=200)
    purchase_date = models.DateField('date purchased')
    color = models.ManyToManyField(Color, related_name='articles')
    article_type = models.ForeignKey(ArticleType, verbose_name='type', related_name='articles')
    cost = models.DecimalField(max_digits=6, decimal_places=2)
    size = models.CharField(max_length=30)
    purchase_location = models.ForeignKey(Store, verbose_name='purchase location',
        related_name='articles', on_delete=models.PROTECT)

    class Meta:
        ordering = ['name']


    def worn_with(self):
        articles = (Article.objects.filter(outfits__articles__id=self.id) |
            Article.objects.filter(accessorized_outfits__articles__id=self.id))
        return articles.distinct().exclude(id=self.id).order_by('name')

    def bought_on_or_before(self, date):
        return self.purchase_date <= date

    def __unicode__(self):
        return self.name


class Outfit(models.Model):
    articles = models.ManyToManyField(Article, related_name='outfits')

    def cost(self):
        return self.articles.aggregate(Sum('cost'))['cost__sum']

    def __unicode__(self):
        return str(self.id) + ": " + ', '.join((f.__unicode__() for f in self.articles.all()))


class AccessorizedOutfit(models.Model):
    base_outfit = models.ForeignKey(Outfit, verbose_name='base outfit',
        related_name='accessorized_outfits')
    articles = models.ManyToManyField(Article, related_name='accessorized_outfits',
        verbose_name='accessories', blank=True)

    def cost(self):
        return (self.base_outfit.articles.aggregate(Sum('cost'))['cost__sum'] +
          self.articles.aggregate(Sum('cost'))['cost__sum'])

    def all_articles(self):
        articles = []
        articles.extend(self.base_outfit.articles.all())
        articles.extend(self.articles.all())
        return articles

    def __unicode__(self):
        return str(self.id) + ': ' + ', '.join((f.__unicode__() for f in self.all_articles()))


class Date(models.Model):
    date = models.DateField('date', unique=True)
    outfits_worn = models.ManyToManyField(AccessorizedOutfit, related_name='dates_worn')

    class Meta:
        ordering = ['date']

    def all_articles(self):
        return (Article.objects.filter(
          Q(outfits__accessorized_outfits__dates_worn=self) |
          Q(accessorized_outfits__dates_worn=self)))

    def articles_bought_before_worn(self):
        l = (lambda article: article.bought_on_or_before(self.date))
        return not all(map(l, self.all_articles()))

    def get_date_id(self):
        return str(self.date)

    def __unicode__(self):
        return str(self.date)

