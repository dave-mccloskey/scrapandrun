from rest_framework import serializers
from clothes.models import *


class DateSerializer(serializers.HyperlinkedModelSerializer):
    photo = serializers.Field(source='first_outfit_photo.src')

    class Meta:
        model = Date
        fields = ('date', 'outfits_worn', 'photo')


class AccessorizedOutfitSerializer(serializers.HyperlinkedModelSerializer):

    """
    Serializer for AccessorizedOutfits.
    """

    class Meta:
        model = AccessorizedOutfit
        fields = ('date', 'outfits_worn')
