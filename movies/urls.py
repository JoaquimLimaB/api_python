from django.urls import path
from . import views

urlpatterns = [
    path('movies/', views.MovieCreateListView.as_view(), name='movie-creat-list'),
    path('movies/<int:pk>/', views.MovieRetriveUpdateDestroyView.as_view(),
         name='movie-detail-view'),
    path('movies/stats/', views.MovieStatsView.as_view(),
         name='movie-stats-view'),
]
