from rest_framework import serializers

from apps.administration.models import AboutUs, Direction, Partner


# AboutUs
class AboutUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutUs
        fields = [
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
        fields = ['title',
                  'description',
                  'title_secondary',
                  'description_secondary',
                  'link',
                  'photo', ]


# Partner
class PartnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partner
        fields = ['title',
                  'description',
                  'link',
                  'logo',
                  'photo', ]
