# Generated by Django 3.2.5 on 2021-11-04 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('empId', models.IntegerField()),
                ('empname', models.CharField(max_length=100)),
                ('empemail', models.EmailField(max_length=100)),
                ('emppass', models.CharField(max_length=100)),
                ('empmobile', models.CharField(max_length=100)),
                ('empaddress', models.CharField(max_length=100)),
            ],
        ),
    ]
