from rest_framework import viewsets
from .models import Concessionnaire, Voiture
from .serializers import ConcessionnaireSerializer, VoitureSerializer

class ConcessionnaireViewSet(viewsets.ModelViewSet):
    queryset = Concessionnaire.objects.all()
    serializer_class = ConcessionnaireSerializer

class VoitureViewSet(viewsets.ModelViewSet):
    queryset = Voiture.objects.all()
    serializer_class = VoitureSerializer
