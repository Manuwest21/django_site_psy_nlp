# Generated by Django 4.2.3 on 2023-07-10 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apppsy', '0004_rename_patient_firstname_le_patient_patient_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Le_patient_date',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_lastname', models.CharField(max_length=255)),
                ('patient_name', models.CharField(max_length=255)),
                ('date', models.DateField()),
                ('predicted', models.CharField(max_length=255)),
                ('confidence', models.FloatField()),
            ],
        ),
    ]