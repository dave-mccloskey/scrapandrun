from clothes.models import *
from django.contrib import admin


class DateAdmin(admin.ModelAdmin):
  filter_vertical = ['outfits_worn']


class OutfitAdmin(admin.ModelAdmin):
  filter_horizontal = ['articles',]
  search_fields = ['articles__name',]


class ArticleAdmin(admin.ModelAdmin):
  filter_horizontal = ['color',]
  
  list_display = ['name', 'article_type', 'purchase_date', 'cost', 'size',]
  search_fields = ['name', 'article_type__name',]


class ColorAdmin(admin.ModelAdmin):
  search_fields = ['name',]


class ArticleTypeAdmin(admin.ModelAdmin):
  pass


class AccessorizedOutfitAdmin(admin.ModelAdmin):
  search_fields = ['base_outfit__articles__name', 'articles__name']
  filter_horizontal = ['articles',]
  raw_id_fields = ['base_outfit',]


class StoreAdmin(admin.ModelAdmin):
  pass


admin.site.register(Date, DateAdmin)
admin.site.register(Outfit, OutfitAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Color, ColorAdmin)
admin.site.register(ArticleType, ArticleTypeAdmin)
admin.site.register(Store, StoreAdmin)
admin.site.register(AccessorizedOutfit, AccessorizedOutfitAdmin)
