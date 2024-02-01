from rest_framework import serializers

from apps.administration.models import AboutUs, Direction, Partner, Service, Banner, Guide


# AboutUs
class AboutUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutUs
        fields = [
            'id',
            'title_uz',
            'title_ru',
            'title_en',
            'description_uz',
            'description_ru',
            'description_en',
            # 'title_secondary',
            # 'description_secondary',
            'link',
            'photo',
        ]


# Service
class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = [
            'id',
            'title_uz',
            'title_ru',
            'title_en',
            'description_uz',
            'description_ru',
            'description_en',
            # 'title_secondary',
            # 'description_secondary',
            'link',
            'photo',
        ]


# Direction
class DirectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Direction
        fields = [
            'id',
            'title_uz',
            'title_ru',
            'title_en',
            'description_uz',
            'description_ru',
            'description_en',
            # 'title_secondary',
            # 'description_secondary',
            'link',
            'photo',
        ]


# Partner
class PartnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partner
        fields = [
            'id',
            'title_uz',
            'title_ru',
            'title_en',
            'description_uz',
            'description_ru',
            'description_en',
            'link',
            'logo',
            'photo',
        ]


# Banner
class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = [
            'id',
            'title_uz',
            'title_ru',
            'title_en',
            'description_uz',
            'description_ru',
            'description_en',
            'photo',
        ]


# Guide
class GuideSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guide
        fields = [
            'id',
            'title_uz',
            'title_ru',
            'title_en',
            'description_uz',
            'description_ru',
            'description_en',
            'link',
        ]
