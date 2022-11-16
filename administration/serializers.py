from rest_framework import serializers
from .models import CB_Driver_Master
from user.models import CB_Trans_Table


class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = CB_Driver_Master
        fields = ('__all__')

class TransSerializer(serializers.ModelSerializer):
    class Meta:
        model = CB_Trans_Table
        fields = ('__all__')