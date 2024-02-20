import factory
from factory.django import DjangoModelFactory

from main.models import *

class RaspolozenjeFactory(DjangoModelFactory):
    class Meta:
        model = Raspolozenje

    mood = factory.Faker("sentence", nb_words = 2)
    notes = factory.Faker("sentence", nb_words = 50)
    datum_izrade = factory.Faker("date_time")


class LijekoviFactory(DjangoModelFactory):
    class Meta:
        model = Lijekovi

    user = factory.Faker("name")
    ime_lijeka = factory.Faker("sentence",nb_words = 1)
    doza = factory.Faker("sentence", nb_words = 2)
    ucestalost = factory.Faker("random_digit")
    datum_izrade = factory.Faker("date_time")
    kategorija = factory.Faker("random_digit", nb_digits = 1)


class JournalEntryFactory(DjangoModelFactory):
    class Meta:
        model = JournalEntry

    user = factory.Faker("name")
    naslov = factory.Faker("sentence", nb_words = 3)
    sadrzaj = factory.Faker("sentence", nb_words = 50)
    datum_izrade = factory.Faker("date_time")


class KategorijaLijekaFactory(DjangoModelFactory):
    class Meta:
        model = KategorijaLijeka

    naziv = factory.Faker("random_digit", nb_digits = 1)

