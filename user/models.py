from django.db import models

# Create your models here.
class AT_transaction(models.Model):
  id_num = models.AutoField(
    primary_key=True
  )

  username = models.TextField(
    max_length=500,
    null=False,
    blank=False
  )

  from_time = models.TimeField(
    max_length=1000,
    null=False,
    blank=False
  )


  to_time = models.TimeField(
    max_length=1000,
    null=False,
    blank=False
  )

  booking_date = models.DateField(
    max_length=1000,
    null=False,
    blank=False
  )

  from_address = models.TextField(
    max_length=1000,
    null=False,
    blank=False
  )

  def __str__(self):
    return self.username