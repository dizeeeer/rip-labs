# Generated by Django 3.1.5 on 2021-01-13 12:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carshowroom', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='car_model',
            old_name='dealer_id',
            new_name='dealer',
        ),
    ]
