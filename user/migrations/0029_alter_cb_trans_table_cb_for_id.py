# Generated by Django 4.1.2 on 2022-10-27 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0028_alter_cb_trans_table_cb_for_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cb_trans_table',
            name='CB_For_ID',
            field=models.IntegerField(),
        ),
    ]
