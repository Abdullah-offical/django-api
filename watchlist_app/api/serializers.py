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
    # watchlist = WatchListSerializer(many=True, read_only=True)
    # watchlist = serializers.StringRelatedField(many=True)
    # watchlist = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    watchlist = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='movie_details'
    )

    class Meta:
        model = StreamPlatform
        fields = "__all__"
