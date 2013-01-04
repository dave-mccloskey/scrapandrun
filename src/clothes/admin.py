from clothes.models import *

from django import forms
from django.contrib import admin

from picasa import PicasaAdminImageWidget

##### Forms for Validation

class MyDateAdminForm(forms.ModelForm):
  class Meta:
    model = Date

  def clean(self):
    cleaned_data = super(MyDateAdminForm, self).clean()
    date = cleaned_data.get("date")
    outfits_worn = cleaned_data.get("outfits_worn")

    errors = []
    for outfit in outfits_worn:
      for article in outfit.all_articles():
        if article.purchase_date > date:
          errors.append(u'%s was bought on %s, after %s' %
            (article.name, str(article.purchase_date), str(date)))
    if len(errors) > 0:
      raise ValidationError(errors)
    return cleaned_data

##### Admin Definitions

class DateAdmin(admin.ModelAdmin):
  form = MyDateAdminForm
  raw_id_fields = ['outfits_worn']


class OutfitAdmin(admin.ModelAdmin):
  filter_horizontal = ['articles', ]
  search_fields = ['articles__name', ]


class ArticleAdmin(admin.ModelAdmin):
  filter_horizontal = ['color', ]

  list_display = ['name', 'article_type', 'purchase_date', 'cost', 'size', ]
  search_fields = ['name', 'article_type__name', ]


class ColorAdmin(admin.ModelAdmin):
  search_fields = ['name', ]


class ArticleTypeAdmin(admin.ModelAdmin):
  pass


class AccessorizedOutfitAdmin(admin.ModelAdmin):
  search_fields = ['base_outfit__articles__name', 'articles__name']
  filter_horizontal = ['articles', ]
  raw_id_fields = ['base_outfit', ]


class StoreAdmin(admin.ModelAdmin):
  pass


admin.site.register(Date, DateAdmin)
admin.site.register(Outfit, OutfitAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Color, ColorAdmin)
admin.site.register(ArticleType, ArticleTypeAdmin)
admin.site.register(Store, StoreAdmin)
admin.site.register(AccessorizedOutfit, AccessorizedOutfitAdmin)

