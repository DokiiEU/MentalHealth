from django import forms
from .models import KorisnikLijek, Lijekovi, Raspolozenje, JournalEntry

class LijekForm(forms.ModelForm):
    lijek = forms.ModelChoiceField(queryset=Lijekovi.objects.all(), label='Ime lijeka')

    class Meta:
        model = KorisnikLijek
        fields = ['korisnik', 'lijek']

class RaspolozenjeForm(forms.ModelForm):

    class Meta:
        model = Raspolozenje
        fields = ['korisnik', 'mood', 'notes']

class DnevnikForm(forms.ModelForm):

    class Meta:
        model = JournalEntry
        fields = ['user', 'naslov', 'sadrzaj']