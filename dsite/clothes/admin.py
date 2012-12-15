from clothes.models import Date, Outfit, Article, Color, ArticleType, AccessorizedOutfit, Store
from django.contrib import admin


class ClothesAdmin(admin.ModelAdmin):
    pass


class OutfitAdmin(admin.ModelAdmin):
    pass


class ArticleAdmin(admin.ModelAdmin):
    pass


class ColorAdmin(admin.ModelAdmin):
    pass


class ArticleTypeAdmin(admin.ModelAdmin):
    pass


class AccessorizedOutfitAdmin(admin.ModelAdmin):
    pass


class StoreAdmin(admin.ModelAdmin):
    pass


admin.site.register(Date, ClothesAdmin)
admin.site.register(Outfit, OutfitAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Color, ColorAdmin)
admin.site.register(ArticleType, ArticleTypeAdmin)
admin.site.register(Store, StoreAdmin)
admin.site.register(AccessorizedOutfit, AccessorizedOutfitAdmin)
