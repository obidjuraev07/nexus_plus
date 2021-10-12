from rest_framework import serializers
from.models import Region, District

class RegionSerializers(serializers.ModelSerializer):
    model =Region
    fields = ["name"]

class DistrictSerializers(serializers.ModelSerializer):
    pass