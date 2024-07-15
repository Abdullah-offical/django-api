from django.urls import path

# from watchlist_app.api.views import movie_list, movie_details

# class base view 
from watchlist_app.api.views import MovieListAV, MovieDetailAV

urlpatterns = [
    # path('list/', movie_list, name='movie_list'),
    # path('<int:pk>/', movie_details, name='movie_details'),

# -------- For Class Base View --------
    path('list/', MovieListAV.as_view(), name='movie_list'),
    path('<int:pk>/', MovieDetailAV.as_view(), name='movie_details'),
]
