from dataclasses import field
from pyexpat import model
from rest_framework import serializers
from user.models import user_transactions

class BookingSerializer(serializers.Serializer):
    class Meta:
        model = user_transactions
        fields = ('id_num', 'username', 'from_time', 'to_time', 'booking_date', 'from_address')
