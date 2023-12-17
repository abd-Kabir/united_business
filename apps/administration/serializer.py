from rest_framework import serializers

from apps.administration.models import AboutUs, Direction, Partner


# AboutUs
class AboutUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutUs
        fields = ['title',
                  'description',
                  'link',
                  'photo', ]


# Direction
class DirectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Direction
        fields = ['title',
                  'description',
                  'link',
                  'photo', ]


# Partner
class PartnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partner
        fields = ['title',
                  'description',
                  'photo_1',
                  'photo_2', ]
