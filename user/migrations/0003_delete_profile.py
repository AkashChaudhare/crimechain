# Generated by Django 4.1.7 on 2023-02-17 16:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_profile_agency_profile_agency_id'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
