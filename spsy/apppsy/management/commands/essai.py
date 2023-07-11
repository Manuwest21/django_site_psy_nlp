from django.core.management.base import BaseCommand
from django.db import transaction
from apppsy.models import Le_patient_date
import pandas as pd

class Command(BaseCommand):
    help = 'Import patients from CSV file'

    def handle(self, *args, **options):
        df = pd.read_csv('emo2.csv')
        df.rename(columns={'patient_firstname': 'patient_name'}, inplace=True)

        with transaction.atomic():
            for index, row in df.iterrows():
                patient = Le_patient_date(
                    patient_lastname=row['patient_lastname'],
                    patient_name=row['patient_name'],
                    predicted=row['predicted'],
                    confidence=row['confidence'],
                    date=row['Date']
                )
                patient.save()

        self.stdout.write(self.style.SUCCESS('Patients imported successfully'))
