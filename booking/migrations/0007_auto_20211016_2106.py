# Generated by Django 3.2.8 on 2021-10-16 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0006_alter_booking_instructor_requested'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='approved',
            field=models.IntegerField(choices=[('No', 0), ('Yes', 1)], default='No'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='instructor_requested',
            field=models.CharField(choices=[('No', 0), ('Yes', 1)], max_length=5),
        ),
    ]
