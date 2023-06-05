from django.urls import path
from . import views

urlpatterns = [
    path('predict/', views.create_person, name='create_person'),
    path('person/<str:name>/', views.get_person_data, name='get_person_data'),
]
