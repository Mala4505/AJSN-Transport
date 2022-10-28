from django import forms
from .models import *

class Form_CB_Trans_Table(forms.ModelForm):
    class Meta:
        model= CB_Trans_Table
        fields= ["dt", "UserId", "CB_For_ID", "No_Of_Passenger", "Source", "Destination", "Purpose", "Time_From", "Time_To", "Actual_Time_To", "CBStatus", "CarId", "Driver_ID", "StartKm", "EndKm", "TotalKmTravelled", "Estimated_Amt", "Actual_Amt", "Payment_ID", "Payment_Ref_Id", "Payment_Status", "Submitted_By", "Overtime", "Overtime_Time", "TimeStamp"]


class Form_CB_Option_Master(forms.ModelForm):
    class Meta:
        model= CB_Option_Master
        fields= ["CB_For_ID","CB_For"]