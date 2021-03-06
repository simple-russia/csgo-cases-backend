from django.urls import path, include
from . import views

urlpatterns = [
    path('get-all-cases', views.get_cases_view),
    path('get-weapons', views.get_weapons_view),
    path('search', views.search_view),
    path('create', views.create_view),
]

