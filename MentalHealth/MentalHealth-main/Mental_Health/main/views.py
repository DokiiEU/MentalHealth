from django.views import View
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import redirect, render, get_list_or_404    
from django.urls import reverse_lazy


from main.models import Lijekovi, Raspolozenje, JournalEntry, KorisnikLijek
class HomePageView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'home.html')

def landing_page(request):
    return render(request, 'home.html')


class LoginPageView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'login.html')

def landing_page(request):
    return render(request, 'login.html')

class MainPageView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'mainpage.html')

def landing_page(request):
    return render(request, 'mainpage.html')

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login

class RegisterPageView(View):
    def get(self, request, *args, **kwargs):
        form = UserCreationForm()
        return render(request, 'registration/register.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('../mainpage') 
        return render(request, 'registration/register.html', {'form': form})
    

class JournalEntryView(ListView):
    model = JournalEntry

class KorisnikLijekView(ListView):
    model = KorisnikLijek

class LijekoviView(ListView):
    model = Lijekovi

class RaspolozenjeView(ListView):
    model = Raspolozenje

from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from main.forms import LijekForm, RaspolozenjeForm, DnevnikForm

class LijekCreateView(CreateView):
    model = KorisnikLijek
    form_class = LijekForm
    template_name = 'add_lijekovi.html'
    success_url = reverse_lazy('main:klijek')


class RaspolozenjeUpdateView(UpdateView):
    model = Raspolozenje
    form_class = RaspolozenjeForm
    template_name = 'update_raspolozenje.html'
    success_url = reverse_lazy('main:raspolozenje')


class RaspolozenjeCreateView(CreateView):
    model = Raspolozenje
    form_class = RaspolozenjeForm
    template_name = 'add_raspolozenje.html'
    success_url = reverse_lazy('main:raspolozenje')

class DnevnikCreateView(CreateView):
    model = JournalEntry
    form_class = DnevnikForm
    template_name = 'add_dnevnik.html'
    success_url = reverse_lazy('main:dnevnik')

class DnevnikUpdateView(UpdateView):
    model = JournalEntry
    form_class = DnevnikForm
    template_name = 'update_dnevnik.html'
    success_url = reverse_lazy('main:dnevnik')

class RaspolozenjeDeleteView(DeleteView):
    model = Raspolozenje
    template_name = 'delete_raspolozenje.html'
    success_url = reverse_lazy('main:raspolozenje')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['raspolozenje'] = self.get_object()
        return context

class DnevnikDeleteView(DeleteView):
    model = JournalEntry
    template_name = 'delete_dnevnik.html'
    success_url = reverse_lazy('main:dnevnik')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['dnevnik'] = self.get_object()
        return context

class LijekDeleteView(DeleteView):
    model = KorisnikLijek
    template_name = 'delete_lijekovi.html'
    success_url = reverse_lazy('main:klijek')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['klijek'] = self.get_object()
        return context
