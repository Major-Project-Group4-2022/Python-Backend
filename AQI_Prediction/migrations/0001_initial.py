# Generated by Django 4.1 on 2022-08-28 03:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('_id', models.AutoField(primary_key=True, serialize=False)),
                ('Date', models.DateField(auto_now_add=True)),
                ('city', models.CharField(max_length=20)),
                ('Avg_temp', models.IntegerField()),
                ('Max_temp', models.IntegerField()),
                ('Min_temp', models.IntegerField()),
                ('Humidity', models.IntegerField()),
                ('Visibility', models.IntegerField()),
                ('Wind_speed', models.IntegerField()),
                ('Suspended_windspeed', models.IntegerField()),
                ('PM25', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('_id', models.AutoField(primary_key=True, serialize=False)),
                ('Date', models.DateField(auto_now_add=True)),
                ('FirstName', models.CharField(max_length=30)),
                ('LastName', models.CharField(max_length=30)),
                ('MobileNo', models.CharField(max_length=10)),
                ('EmailId', models.CharField(max_length=50)),
                ('UserName', models.CharField(max_length=30)),
                ('Password', models.CharField(max_length=30)),
            ],
        ),
    ]
