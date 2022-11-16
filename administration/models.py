from django.db import models

class CB_Driver_Master(models.Model):

  Driver_ID = models.AutoField(
    primary_key=True,
    null=False
  )
  
  Driver_Name = models.CharField(
    max_length=100,
    blank=True
  )

  Mobile = models.IntegerField(blank=True, default="")
  
  Email = models.CharField(
    max_length=255,
    blank=True
  )
  
  Address = models.CharField(
    max_length=255,
    blank=True
  )

  Active = models.SmallIntegerField(blank=True, default=0)

  class Meta:
    db_table = 'CB_Driver_Master'