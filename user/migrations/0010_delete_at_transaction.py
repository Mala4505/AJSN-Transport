# Generated by Django 4.1.2 on 2022-10-24 14:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0009_alter_at_transaction_table'),
    ]

    operations = [
        migrations.DeleteModel(
            name='AT_transaction',
        ),
    ]
