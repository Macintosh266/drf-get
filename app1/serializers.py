from django.contrib.auth import authenticate
from django.contrib.messages import success
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

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self,attrs):
        username = attrs.get('username')
        password = attrs.get('password')

        try:
            user=User.objects.get(username=username)
        except User.DoesNotExist:
            raise serializers.ValidationError(
                {
                "succes":False,
                "detail":"User does not exist!"

            })
        auth_user=authenticate(username=user.username,password=password)

        if auth_user is None:
            raise serializers.ValidationError(
                {
                    "succes":False,
                    "detail":"Username or Password is invalid!"
                }
            )

        attrs['user']=auth_user
        return attrs