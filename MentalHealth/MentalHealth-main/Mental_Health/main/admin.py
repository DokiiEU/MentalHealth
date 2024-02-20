from django.contrib import admin
from main.models import *
# Register your models here.

model_list = [Raspolozenje, JournalEntry, Lijekovi, KategorijaLijeka, KorisnikLijek]
admin.site.register(model_list)