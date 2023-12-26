from rest_framework import serializers
from .models import Concessionnaire, Voiture

class ConcessionnaireSerializer(serializers.ModelSerializer):
    class Meta:
        model = Concessionnaire
        fields = ['nom', 'siret', 'code_postal']


    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation.pop('siret', None)
        return representation

class VoitureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Voiture
        fields = ['marque', 'modele', 'chevaux', 'concessionnaire']
