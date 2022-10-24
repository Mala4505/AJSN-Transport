from django.db import models

# Create your models here.
class user_transactions(models.Model):
  id_num = models.AutoField(
    primary_key=True
  )

  username = models.TextField(
    max_length=255,
    null=False,
    blank=False
  )

  from_time = models.TextField(
    max_length=1000,
    null=False,
    blank=False
  )


  to_time = models.TextField(
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

#   class Meta:
#     db_table = 'ajsn_transactions'