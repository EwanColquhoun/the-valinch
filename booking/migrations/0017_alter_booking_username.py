# Generated by Django 3.2.8 on 2021-10-22 21:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('booking', '0016_auto_20211022_2119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='username',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
