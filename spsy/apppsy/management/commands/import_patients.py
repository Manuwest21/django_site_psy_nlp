# from django.core.management.base import BaseCommand
# from apppsy.models import Patient
# from apppsy.models import PatientIndex

# class Command(BaseCommand):
#     help = 'Importer les patients depuis Elasticsearch dans la base de données'

#     def handle(self, *args, **options):
#         # Supprimer tous les patients existants dans la base de données
#         Patient.objects.all().delete()

#         # Récupérer tous les patients depuis l'index Elasticsearch
#         patients = PatientIndex.search().scan()

#         # Ajouter les patients dans la base de données
#         for patient in patients:
#             patient_instance = Patient(
#                 patient_lastname=patient.patient_lastname,
#                 patient_firstname=patient.patient_firstname,
#                 text=patient.text,
#                 date=patient.date,
#                 patient_left=patient.patient_left,
#                 emotion=patient.emotion,
#                 confidence=patient.confidence
#             )
#             patient_instance.save()

#         self.stdout.write(self.style.SUCCESS('Les patients ont été ajoutés à la base de données avec succès.'))
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
