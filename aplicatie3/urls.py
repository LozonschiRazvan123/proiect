from django.urls import path

from aplicatie3 import views

app_name='jobs'

urlpatterns=[
    path('', views.JobView.as_view(), name='lista_joburi'),
    path('adaugare/',views.CreateJobsView.as_view(), name='adauga'),
    path('<int:pk>/update', views.UpadteJobView.as_view(), name='modifica'),
    path('<int:pk>/stergere',views.delete_job,name="sterge"),
    path('<int:pk>/activeaza',views.activate_job,name="activeaza"),
]