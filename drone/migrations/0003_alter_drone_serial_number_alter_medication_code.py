# Generated by Django 4.0.5 on 2022-06-04 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drone', '0002_alter_medication_picture_dispacherdrone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drone',
            name='serial_number',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='medication',
            name='code',
            field=models.CharField(max_length=5, unique=True),
        ),
    ]