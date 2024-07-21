from rest_framework import serializers
from watchlist_app.models import WatchList, StreamPlatform


class StreamPlatformSerializer(serializers.ModelSerializer):
    class Meta:
        model = StreamPlatform
        fields = "__all__"


class WatchSerializer(serializers.ModelSerializer):
    
    

    class Meta:
        model = WatchList
        # all fields show
        fields = "__all__"
        # exclude field not show active
        # exclude = ['active']

    