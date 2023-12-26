from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ConcessionnaireViewSet, VoitureViewSet

router = DefaultRouter()
router.register(r'concessionnaires', ConcessionnaireViewSet)
router.register(r'voitures', VoitureViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
