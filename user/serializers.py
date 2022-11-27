from rest_framework import serializers
from .models import CB_Trans_Table


class TransSerializer(serializers.ModelSerializer):
    class Meta:
        model = CB_Trans_Table
        fields = ('__all__')