from rest_framework.serializers import ModelSerializer, SerializerMethodField

from .models import Car


class CarSerializer(ModelSerializer):
    category = SerializerMethodField()
    engine = SerializerMethodField()

    class Meta:
        model = Car
        fields = '__all__'

    def get_category(self, obj):
        return obj.get_category_display()

    def get_engine(self, obj):
        return obj.get_engine_display()


class CarCreateSerializer(ModelSerializer):

    class Meta:
        model = Car
        fields = '__all__'
