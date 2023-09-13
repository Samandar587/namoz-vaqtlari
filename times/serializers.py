from rest_framework import serializers
from .models import Salah, Mosque, PrayerTime

class SalahSerializer(serializers.ModelSerializer):

    class Meta:
        model = Salah
        fields = '__all__'

class MosqueSerializer(serializers.ModelSerializer):

    class Meta:
        model = Mosque
        fields = '__all__'


class PrayerTimeSerializer(serializers.ModelSerializer):

    mosque = MosqueSerializer()

    def create(self, validate_data):
        mosque_data = validate_data.pop('mosque')

        mosque_instance, _ = Mosque.objects.get_or_create(**mosque_data)
        prayer_time = PrayerTime.objects.create(mosque=mosque_instance, **validate_data)

        return prayer_time

    class Meta:
        model = PrayerTime
        fields = '__all__'