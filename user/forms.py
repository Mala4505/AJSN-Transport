from django import forms
from .models import user_transactions

class Form_user_transactions(forms.ModelForm):
    class Meta:
        model= user_transactions
        fields= ["username", "from_time", "to_time", "booking_date", "from_address"]