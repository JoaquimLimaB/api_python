from django.urls import path
from . import views

urlpatterns = [
    path('genres/', views.GenreCreateListView.as_view(),
         name='genre-create-list'),
    # int:pk --> é referente a chave primaria no caso o id; int de inteiro e pk de Primare Key.
    path('genres/<int:pk>/', views.GenereRetriveUpdateView.as_view(),
         name='genre-datail-view'),
]
