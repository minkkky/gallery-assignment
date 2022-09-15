from rest_framework import serializers

from .models import User as UserModel
from .models import Artist as ArtistModel

from datetime import datetime


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserModel
        fields = ["username", "password"]
        extra_kwargs = {
            "password": {"write_only": True}
        }

    def create(self, validated_data):
        password = validated_data.pop("password", None)
        user = UserModel(**validated_data)
        user.set_password(password)
        user.save()
        return user

class ArtistPostSerializer(serializers.ModelSerializer):

    class Meta:
        model = ArtistModel
        fields = ["user", "name", "gender", "birth", "email", "phone", "is_artist"]


class ArtistSerializer(serializers.ModelSerializer):
    gender = serializers.CharField(source='get_gender_display', read_only=True)
    age = serializers.SerializerMethodField()

    def get_age(self, obj):
        now = int(datetime.today().strftime('%Y'))
        birth = obj.birth.year
        return now-birth

    class Meta:
        model = ArtistModel
        fields = ["user", "name", "gender", "birth", "age", "email", "phone", "is_artist"]


