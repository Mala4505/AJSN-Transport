from django.db import models

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

  CB_For_ID = models.IntegerField(null=False)

  No_Of_Passenger = models.IntegerField()

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
    max_length=6
  )

  CBStatus = models.CharField(
    max_length=20,
    null=False,
    blank=False
  )

  CarId = models.IntegerField()

  Driver_ID = models.IntegerField()

  StartKm = models.IntegerField()

  EndKm = models.IntegerField()

  TotalKmTravelled = models.IntegerField()

  Estimated_Amt = models.FloatField()

  Actual_Amt = models.FloatField()

  Payment_ID = models.IntegerField()

  Payment_Ref_Id = models.IntegerField()

  Payment_Status = models.CharField(
    max_length=15
  )

  Submitted_By = models.CharField(
    max_length=8
  )

  Overtime = models.SmallIntegerField(
    null=False,
    blank=False
  )

  Overtime_Time = models.TimeField(
    max_length=6
  )

  TimeStamp = models.DateTimeField()


  class Meta:
    db_table = 'CB_Trans_Table'



class CB_Option_Master(models.Model):

  CB_For_Id = models.AutoField(
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