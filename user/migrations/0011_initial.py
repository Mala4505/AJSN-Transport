# Generated by Django 4.1.2 on 2022-10-24 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0010_delete_at_transaction'),
    ]

    operations = [
        migrations.CreateModel(
            name='AT_transaction',
            fields=[
                ('id_num', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.TextField(max_length=255)),
                ('from_time', models.TimeField(max_length=1000)),
                ('to_time', models.TimeField(max_length=1000)),
                ('booking_date', models.DateField(max_length=1000)),
                ('from_address', models.TextField(max_length=1000)),
            ],
            options={
                'db_table': 'AT_transaction',
            },
        ),
    ]
