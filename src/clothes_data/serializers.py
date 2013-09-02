from rest_framework import serializers
from clothes.models import *


class DateSerializer(serializers.HyperlinkedModelSerializer):
    photo = serializers.SerializerMethodField('get_photo_url')

    class Meta:
        model = Date
        fields = ('date', 'outfits_worn', 'photo')

    def get_photo_url(self, obj):
        photo = obj.first_outfit_photo()
        return photo.src(700) if photo else ""


class AccessorizedOutfitSerializer(serializers.HyperlinkedModelSerializer):

    """
    Serializer for AccessorizedOutfits.
    """

    class Meta:
        model = AccessorizedOutfit
        fields = ('date', 'outfits_worn')
