# Generated by Django 4.2.3 on 2023-07-10 12:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apppsy', '0003_le_patient'),
    ]

    operations = [
        migrations.RenameField(
            model_name='le_patient',
            old_name='patient_firstname',
            new_name='patient_name',
        ),
    ]
