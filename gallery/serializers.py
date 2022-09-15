from rest_framework import serializers

from .models import Art as ArtModel
from .models import Exbihition as ExbihitionModel
from user.models import Artist as ArtistModel

from datetime import datetime


class ArtSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()

    def get_name(self, obj):
        return ArtistModel.objects.get(id=obj.artist.id).name

    class Meta:
        model = ArtModel
        fields = ["id", "artist", "title", "price", "size", "name"]


class ExbihitionSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()

    def get_name(self, obj):
        return ArtistModel.objects.get(id=obj.artist.id).name

    class Meta:
        model = ExbihitionModel
        fields = ["artist", "title", "start", "end", "arts", "name"]


