import pandas as pd
from apppsy.models import Le_patient_date
df = pd.read_csv('emo2.csv')

data = df.to_dict('records')

for row in data:
    instance = Le_patient_date(**row)
    instance.save()