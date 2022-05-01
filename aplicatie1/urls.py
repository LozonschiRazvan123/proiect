from django.urls import path

from aplicatie1 import views

app_name='locations'

urlpatterns=[
    path('', views.LocationView.as_view(), name='lista_locatii'),
    path('adaugare/',views.CreateLocationsView.as_view(), name='adauga'),
    path('<int:pk>/update', views.UpadteLocationView.as_view(), name='modifica'),
    path('<int:pk>/stergere',views.delete_location,name="sterge"),
    path('<int:pk>/activeaza',views.activate_location,name="activeaza"),
]