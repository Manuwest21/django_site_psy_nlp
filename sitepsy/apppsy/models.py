from django.db import models
from django.contrib.auth.models import User

class Note(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
	
    def __str__(self):
        return self.title

# Create your models here.
from django.db import models
from django.conf import settings
from elasticsearch_dsl import Document, Text, Date, Boolean, Keyword, Float, connections

# Configurer la connexion Elasticsearch
connections.create_connection(hosts=settings.ELASTICSEARCH_DSL['default']['hosts'])


# Modèle Django pour Patient predicted,confidence,patient_name,patient_lastname
class Patient(models.Model):
    patient_lastname = models.CharField(max_length=255)
    patient_firstname = models.CharField(max_length=255)
    text = models.TextField()
    date = models.DateField()
    patient_left = models.BooleanField()
    emotion = models.CharField(max_length=255)
    confidence = models.FloatField()
    # Ajoutez d'autres champs de modèle selon vos besoins

    def save(self, *args, **kwargs):
        # Appeler la méthode save() du modèle pour enregistrer les données dans la base de données
        super().save(*args, **kwargs)

        # Indexer les données dans Elasticsearch après l'enregistrement
        patient_doc = PatientIndex(
            meta={'id': self.id},
            patient_lastname=self.patient_lastname,
            patient_firstname=self.patient_firstname,
            text=self.text,
            date=self.date,
            patient_left=self.patient_left,
            emotion=self.emotion,
            confidence=self.confidence
        )
        patient_doc.save()

    def delete(self, *args, **kwargs):
        # Supprimer l'instance du modèle Patient
        super().delete(*args, **kwargs)

        # Supprimer les données correspondantes de l'index Elasticsearch
        patient_doc = PatientIndex.get(id=self.id)
        patient_doc.delete()


# Index Elasticsearch pour le modèle Patient
class PatientIndex(Document):
    patient_lastname = Keyword()
    patient_firstname = Keyword()
    text = Text(analyzer='standard')
    date = Date()
    patient_left = Boolean()
    emotion = Keyword()
    confidence = Float()

    class Index:
        name = 'notes'  # Nom de l'index Elasticsearch pour votre modèle Patient

    class Meta:
        mappings = {
            "properties": {
                "patient_lastname": {"type": "keyword"},
                "patient_firstname": {"type": "keyword"},
                "text": {"type": "text", "analyzer": "standard"},
                "date": {"type": "date"},
                "patient_left": {"type": "boolean"},
                "emotion": {"type": "keyword"},
                "confidence": {"type": "float"}
            }
        }

        mappings = {
            "properties": {
                "patient_lastname": {"type": "keyword"},
                "patient_firstname": {"type": "keyword"},
                "text": {"type": "text", "analyzer": "standard"},
                "date": {"type": "date"},
                "patient_left": {"type": "boolean"},
                "emotion": {"type": "keyword"},
                "confidence": {"type": "float"}
            }
        }

class Le_patient(models.Model):
    patient_lastname = models.CharField(max_length=255)
    patient_name = models.CharField(max_length=255)
    
    
    
    predicted = models.CharField(max_length=255)
    confidence = models.FloatField()