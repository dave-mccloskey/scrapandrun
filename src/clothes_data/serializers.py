from rest_framework import serializers
from clothes.models import *


class DateSerializer(serializers.HyperlinkedModelSerializer):

    """
    Serializer for Dates.
    """

    class Meta:
        model = Date
        fields = ('date', 'outfits_worn')
