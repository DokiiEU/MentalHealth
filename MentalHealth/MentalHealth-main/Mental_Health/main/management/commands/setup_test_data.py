import random

from django.core.management.base import BaseCommand
from django.db import transaction
from django.contrib.auth.models import User

from main.models import Raspolozenje, Lijekovi, JournalEntry, KategorijaLijeka
from main.factories import RaspolozenjeFactory, LijekoviFactory, JournalEntryFactory, KategorijaLijekaFactory


NUM_RASPOLOZENJA = 15
NUM_LIJEKOVI = 20
NUM_JOURNAL_ENTRIES = 50
NUM_KATEGORIJE_LIJEKOVA = 5

class Command(BaseCommand):
    help = "Generira testne podatke"

    @transaction.atomic
    def handle(self, *args, **kwargs):
        self.stdout.write("Brisanje starih podataka...")
        models = [Raspolozenje, Lijekovi, JournalEntry, KategorijaLijeka]
        for m in models:
            m.objects.all().delete()

        self.stdout.write("Stvaranje novih podataka...")

        # Dohvati sve korisnike iz baze
        korisnici = User.objects.all()

        for _ in range(NUM_RASPOLOZENJA):
            # Nasumično odaberi korisnika
            korisnik = random.choice(korisnici)
            # Stvori raspoloženje za odabranog korisnika
            raspolozenje = RaspolozenjeFactory(korisnik=korisnik)

        for _ in range(NUM_LIJEKOVI):
            korisnik = random.choice(korisnici)
            lijek = LijekoviFactory(user=korisnik)

        for _ in range(NUM_JOURNAL_ENTRIES):
            korisnik = random.choice(korisnici)
            entry = JournalEntryFactory(user=korisnik)

        for _ in range(NUM_KATEGORIJE_LIJEKOVA):
            kategorija = KategorijaLijekaFactory()
