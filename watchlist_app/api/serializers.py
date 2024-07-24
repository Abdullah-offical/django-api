from rest_framework import serializers
from watchlist_app.models import WatchList, StreamPlatform




class WatchListSerializer(serializers.ModelSerializer):    
    class Meta:
        model = WatchList
        # all fields show
        fields = "__all__"
        # exclude field not show active
        # exclude = ['active']

class StreamPlatformSerializer(serializers.ModelSerializer):
    watchlist = WatchListSerializer(many=True, read_only=True)
    class Meta:
        model = StreamPlatform
        fields = "__all__"
