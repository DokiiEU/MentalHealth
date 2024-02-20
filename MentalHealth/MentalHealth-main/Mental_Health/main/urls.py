from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('mainpage/', views.MainPageView.as_view(), name= 'mainpage'),
    path('register/', views.RegisterPageView.as_view(), name= 'register'),
    path('dnevnik/', views.JournalEntryView.as_view(), name='dnevnik'),
    path('lijekovi/', views.LijekoviView.as_view(), name='lijekovi'),
    path('klijek/', views.KorisnikLijekView.as_view(), name='klijek'),
    path('raspolozenje/', views.RaspolozenjeView.as_view(), name='raspolozenje'),
    path('add/', views.LijekCreateView.as_view(), name='add'),
    path('update/<int:pk>', views.RaspolozenjeUpdateView.as_view(), name='update'),
    path('addr/', views.RaspolozenjeCreateView.as_view(), name='addr'),
    path('addd/', views.DnevnikCreateView.as_view(), name='addd'),
    path('updated/<int:pk>', views.DnevnikUpdateView.as_view(), name='updated'),
    path('deleter/<int:pk>', views.RaspolozenjeDeleteView.as_view(), name='deleter'),
    path('deleted/<int:pk>', views.DnevnikDeleteView.as_view(), name='deleted'),
    path('delete/<int:pk>', views.LijekDeleteView.as_view(), name='delete')














]