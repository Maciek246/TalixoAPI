from django.utils.dateformat import datetime
from rest_framework.serializers import ModelSerializer, SerializerMethodField, ValidationError

from .models import Car


class CarSerializer(ModelSerializer):
    category = SerializerMethodField()
    engine = SerializerMethodField()

    class Meta:
        model = Car
        fields = ('pk', 'registration', 'max_passengers', 'year_of_production',
                  'producer', 'model', 'type', 'category', 'engine')
        read_only_fields = ('pk',)

    def get_category(self, obj):
        return obj.get_category_display()

    def get_engine(self, obj):
        return obj.get_engine_display()


class CarCreateSerializer(ModelSerializer):

    class Meta:
        model = Car
        fields = ('pk', 'registration', 'max_passengers', 'year_of_production',
                  'producer', 'model', 'type', 'category', 'engine')
        read_only_fields = ('pk',)

    def validate(self, attrs):
        if attrs['year_of_production'] > datetime.datetime.today().year:
            raise ValidationError('Bad year of production car', 400)
        return attrs
