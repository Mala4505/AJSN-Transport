# Generated by Django 4.1.2 on 2022-10-18 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AJSN_tIme_range',
            fields=[
                ('id_num', models.AutoField(primary_key=True, serialize=False)),
                ('from_time', models.TimeField(max_length=1000)),
                ('to_time', models.TimeField(max_length=1000)),
                ('from_address', models.TextField(max_length=1000)),
            ],
            options={
                'db_table': 'AJSN_tIme_range',
            },
        ),
    ]
