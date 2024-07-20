from rest_framework import serializers
from watchlist_app.models import Movie


class MovieSerializer(serializers.ModelSerializer):
    len_name = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        # all fields show
        fields = "__all__"
        # exclude field not show active
        # exclude = ['active']

    def get_len_name(Self, object):
        return len(object.name)


    def validate_name(self, value):
        if len(value) < 2:
            raise serializers.ValidationError("Name is to short")
        else:
            return value

    def validate(self, data):
        if data['name'] == data['description']:
            raise serializers.ValidationError('Name and Discription souhd be diffrent')
        else:
            return data
