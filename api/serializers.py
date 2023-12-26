from rest_framework import serializers
from .models import Concessionnaire, Voiture

class ConcessionnaireSerializer(serializers.ModelSerializer):
    class Meta:
        model = Concessionnaire
        fields = ['nom', 'siret', 'code_postal']

class VoitureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Voiture
        fields = ['marque', 'modele', 'chevaux', 'concessionnaire']
