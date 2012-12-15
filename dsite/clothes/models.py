from django.db import models
import datetime


class Store(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=100)
    
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

    def __unicode__(self):
        return self.name + " (" + self.get_basic_color_display() + ")"


class ArticleType(models.Model):
    name = models.CharField(max_length=50)
    
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
    
    def __unicode__(self):
        return self.name


class Outfit(models.Model):
    articles = models.ManyToManyField(Article, related_name='outfits')
    
    def __unicode__(self):
        return str(self.id) + ": " + ', '.join((f.__unicode__() for f in self.articles.all()))


class AccessorizedOutfit(models.Model):
    base_outfit = models.ForeignKey(Outfit, verbose_name='base outfit', related_name='accessorized_outfits')
    articles = models.ManyToManyField(Article, related_name='accessorized_outfits')


class Date(models.Model):
    date = models.DateField('date', unique=True)
    outfits_worn = models.ManyToManyField(AccessorizedOutfit, related_name='dates_worn')
    
    def get_date_id(self):
        return str(self.date)
    
    def __unicode__(self):
        return str(self.date)
