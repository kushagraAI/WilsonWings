from  rest_framework import serializers
from .models import Destination


class DestinationSerializer(serializers.ModelSerializer):

    class Meta():
        model = Destination
        fields = '__all__'


    def validate_name(self, value):
        if not value:
            raise serializers.ValidationError("Name field cannot be empty.")
        if len(value) < 3:
            raise serializers.ValidationError("Name must be at least 3 characters long.")
        return value
