from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import User

class Korisnik(AbstractUser):
    ime = models.CharField(max_length=30)
    prezime = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    datum_rodenja = models.DateField(null=True, blank=True)

    def str(self):
        return self.username

class Raspolozenje(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    mood = models.CharField(max_length=255)
    notes = models.TextField()
    datum_izrade = models.DateTimeField(auto_now_add=True)

class JournalEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    naslov = models.CharField(max_length=255)
    sadrzaj = models.TextField()
    datum_izrade = models.DateTimeField(auto_now_add=True)

class Lijekovi(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ime_lijeka= models.CharField(max_length=255)
    doza = models.CharField(max_length=50)
    ucestalost = models.CharField(max_length=50)
    datum_izrade = models.DateTimeField(auto_now_add=True)