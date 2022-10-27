from dataclasses import field
from pyexpat import model
from rest_framework import serializers
from user.models import CB_Trans_Table

class BookingSerializer(serializers.Serializer):
    class Meta:
        model = CB_Trans_Table
        fields = ('id_num', 'username', 'from_time', 'to_time', 'booking_date', 'from_address')
