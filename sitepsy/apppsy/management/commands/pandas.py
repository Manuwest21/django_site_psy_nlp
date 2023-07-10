from django.db import transaction
from apppsy.models import Le_patient
import pandas as pd
import numpy as numpy

df=pd.read_csv('emo.csv')
df.rename(columns={'patient_firstname':'patient_name'},inplace=True)

def importer_patients(df):
    for index, row in df.iterrows():
        patient = Le_patient(
            patient_lastname=row['patient_lastname'],
            patient_name=row['patient_name'],
            predicted=row['predicted'],
            confidence=row['confidence']
        )
        patient.save()
        
        
importer_patients(df)