from rest_framework import serializers

from apps.administration.models import AboutUs, Direction, Partner, Service


# AboutUs
class AboutUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutUs
        fields = [
            'id',
            'title',
            'description',
            'title_secondary',
            'description_secondary',
            'link',
            'photo',
        ]


# Service
class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = [
            'id',
            'title',
            'description',
            'title_secondary',
            'description_secondary',
            'link',
            'photo',
        ]


# Direction
class DirectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Direction
        fields = [
            'id',
            'title',
            'description',
            'title_secondary',
            'description_secondary',
            'link',
            'photo',
        ]


# Partner
class PartnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partner
        fields = [
            'id',
            'title',
            'description',
            'link',
            'logo',
            'photo',
        ]
