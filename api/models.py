from django.db import models

class Concessionnaire(models.Model):
    nom = models.CharField(max_length=100)
    siret = models.IntegerField()
    code_postal = models.CharField(max_length=5)

    def __str__(self):
        return self.nom

class Voiture(models.Model):
    marque = models.CharField(max_length=100)
    modele = models.CharField(max_length=100)
    chevaux = models.IntegerField()
    concessionnaire = models.ForeignKey(Concessionnaire, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.marque} {self.modele}"
