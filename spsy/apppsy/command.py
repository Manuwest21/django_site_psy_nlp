from models import Patient
from models import PatientIndex


def handle(self, *args, **options):
        # Supprimer tous les patients existants dans la base de données
        Patient.objects.all().delete()

        # Récupérer tous les patients depuis l'index Elasticsearch
        patients = PatientIndex.search().scan()

        # Ajouter les patients dans la base de données
        for patient in patients:
            patient_instance = Patient(
                patient_lastname=patient.patient_lastname,
                patient_firstname=patient.patient_firstname,
                text=patient.text,
                date=patient.date,
                patient_left=patient.patient_left,
                emotion=patient.emotion,
                confidence=patient.confidence
            )
            patient_instance.save()

        self.stdout.write(self.style.SUCCESS('Les patients ont été ajoutés à la base de données avec succès.'))