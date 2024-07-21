from django.urls import path

# from watchlist_app.api.views import movie_list, movie_details

# class base view 
from watchlist_app.api.views import WatchListAV, WatchDetailAV, StreamPlatformAV, StreamPlatformDetailAV

urlpatterns = [
    # path('list/', movie_list, name='movie_list'),
    # path('<int:pk>/', movie_details, name='movie_details'),

# -------- For Class Base View --------
    path('list/', WatchListAV.as_view(), name='movie_list'),
    path('<int:pk>/', WatchDetailAV.as_view(), name='movie_details'),

    path('stream/', StreamPlatformAV.as_view(), name='stream' ),
    path('<int:pk>/', StreamPlatformDetailAV.as_view(), name='stream_details' ),
]
