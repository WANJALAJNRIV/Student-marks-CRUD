# Generated by Django 4.1.7 on 2023-03-14 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('code', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=13)),
            ],
        ),
        migrations.CreateModel(
            name='UnitEnrollment',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('unit_code', models.CharField(max_length=100)),
                ('student_id', models.IntegerField()),
            ],
        ),
    ]
