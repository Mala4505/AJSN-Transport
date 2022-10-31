from email.policy import default
from django.db import models
from django.utils import timezone


# Create your models here.
class CB_Trans_Table(models.Model):

  CB_Trans_Id = models.AutoField(
    primary_key=True,
    null=False
  )
  dt = models.DateField(null=False)

  UserId = models.CharField(
    max_length=8,
    null=False,
    blank=False
  )

  CB_For_ID = models.IntegerField(blank=False)

  No_Of_Passenger = models.IntegerField(blank=True)

  Source = models.CharField(
    max_length=250,
    null=False,
    blank=False
  )

  Destination = models.CharField(
    max_length=250,
    null=False,
    blank=False
  )

  Purpose = models.CharField(
    max_length=250,
    null=False,
    blank=False
  )

  Time_From = models.TimeField(
    max_length=6,
    null=False,
    blank=False
  )

  Time_To = models.TimeField(
    max_length=6,
    null=False,
    blank=False
  )

  Actual_Time_To = models.TimeField(
    max_length=6,
    blank=True
  )

  CBStatus = models.CharField(
    max_length=20,
    blank=True
    # null=False,
    # blank=False
  )

  CarId = models.IntegerField(blank=True)

  Driver_ID = models.IntegerField(blank=True)

  StartKm = models.IntegerField(blank=True)

  EndKm = models.IntegerField(blank=True)

  TotalKmTravelled = models.IntegerField(blank=True)

  Estimated_Amt = models.FloatField(blank=True)

  Actual_Amt = models.FloatField(blank=True)

  Payment_ID = models.IntegerField(blank=True)

  Payment_Ref_Id = models.IntegerField(blank=True)

  Payment_Status = models.CharField(
    max_length=15,
    blank=True
  )

  Submitted_By = models.CharField(
    max_length=8,
    blank=True
  )

  Overtime = models.SmallIntegerField(blank=True, default=0)

  Overtime_Time = models.TimeField(
    max_length=6,
    blank=True
  )

  TimeStamp = models.DateTimeField(blank=True, default=timezone.now)


  class Meta:
    db_table = 'CB_Trans_Table'



class CB_Option_Master(models.Model):

  CB_For_ID = models.AutoField(
    primary_key=True,
    null=False
  )
  CB_For = models.CharField(
    max_length=20,
    null=False,
    blank=False
  )

  class Meta:
    db_table = 'CB_Option_Master'