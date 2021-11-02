# Generated by Django 3.2.8 on 2021-11-02 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0024_alter_booking_username'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('telephone', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=40)),
                ('message', models.TextField()),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]
