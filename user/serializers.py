from dataclasses import field
from pyexpat import model
from rest_framework import serializers
from user.models import AT_transaction

class BookingSerializer(serializers.Serializer):
    class Meta:
        model = AT_transaction
        fields = ('id_num', 'username', 'from_time', 'to_time', 'booking_date', 'from_address')
