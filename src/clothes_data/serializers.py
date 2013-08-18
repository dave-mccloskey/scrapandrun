from rest_framework import serializers
from clothes.models import *


class DateSerializer(serializers.HyperlinkedModelSerializer):
    photo = serializers.SerializerMethodField('get_photo_url')

    class Meta:
        model = Date
        fields = ('date', 'outfits_worn', 'photo')

    def get_photo_url(self, obj):
        return obj.first_outfit_photo().src(700)


class AccessorizedOutfitSerializer(serializers.HyperlinkedModelSerializer):

    """
    Serializer for AccessorizedOutfits.
    """

    class Meta:
        model = AccessorizedOutfit
        fields = ('date', 'outfits_worn')
