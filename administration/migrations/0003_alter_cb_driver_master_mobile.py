# Generated by Django 4.1.3 on 2022-11-14 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0002_remove_cb_driver_master_id_cb_driver_master_mobile_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cb_driver_master',
            name='Mobile',
            field=models.IntegerField(blank=True, default=''),
        ),
    ]
