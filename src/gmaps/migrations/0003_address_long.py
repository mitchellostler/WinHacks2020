# Generated by Django 3.0 on 2020-03-28 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gmaps', '0002_drive_route'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='long',
            field=models.DecimalField(decimal_places=6, default=0, max_digits=12),
        ),
    ]