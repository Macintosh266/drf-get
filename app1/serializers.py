from rest_framework import serializers
from .models import *

class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Actor
        fields='__all__'


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model=Movie
        fields=['name','year','genre','actor']


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model=CommitMovie
        fields=['title','movie','author']
        read_only_fields = ['author']