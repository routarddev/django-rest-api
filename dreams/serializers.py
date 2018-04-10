from rest_framework import serializers
from .models import Dreams

class DreamsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dreams
        fields = ('dreams_id', 'username', 'dream_date', 'is_lucid')
        