# Generated by Django 4.1.2 on 2022-10-27 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0027_alter_cb_trans_table_overtime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cb_trans_table',
            name='CB_For_ID',
            field=models.IntegerField(blank=True),
        ),
    ]
