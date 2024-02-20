from django.db import models
from django.contrib.auth.models import User

class Raspolozenje(models.Model):
    korisnik = models.OneToOneField(User, on_delete=models.CASCADE)
    mood = models.CharField(max_length=255)
    notes = models.TextField()
    datum_izrade = models.DateTimeField(auto_now_add=True)

class JournalEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    naslov = models.CharField(max_length=255)
    sadrzaj = models.TextField()
    datum_izrade = models.DateTimeField(auto_now_add=True)

class KategorijaLijeka(models.Model):
    naziv = models.CharField(max_length=50)

class Lijekovi(models.Model):
    ime_lijeka= models.CharField(max_length=255)
    doza = models.CharField(max_length=50)
    ucestalost = models.CharField(max_length=50)
    datum_izrade = models.DateTimeField(auto_now_add=True)
    kategorija = models.ForeignKey(KategorijaLijeka, on_delete=models.CASCADE, default = None)

    def __str__(self):
        return self.ime_lijeka


class KorisnikLijek(models.Model):
    korisnik = models.ForeignKey(User, on_delete=models.CASCADE)
    lijek = models.ForeignKey(Lijekovi, on_delete=models.CASCADE)

    class Meta:
        unique_together = ['korisnik', 'lijek']
