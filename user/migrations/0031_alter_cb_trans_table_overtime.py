# Generated by Django 4.1.2 on 2022-10-28 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0030_rename_cb_for_id_cb_option_master_cb_for_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cb_trans_table',
            name='Overtime',
            field=models.SmallIntegerField(blank=True, default=0, max_length=1),
        ),
    ]