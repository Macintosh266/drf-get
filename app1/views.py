from django.db.models import *
from .serializers import *
from django.shortcuts import render,get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import *
import json





# @api_view(['GET','POST'])
# def actor_get_post(request):
#     if request.method == 'GET':
#         actors=Actor.objects.all()
#         serialize=ActorSerializer(actors,many=True)
#         return Response(data=serialize.data, status=status.HTTP_200_OK)
#     elif request.method=='POST':
#         serialize=ActorSerializer(data=request.data)
#         if serialize.is_valid(raise_exception=True):
#             serialize.save()
#             return Response(data=serialize,status=status.HTTP_201_CREATED)
#
#
# @api_view(['PUT'])
# def actor_put(request,pk):
#     actor=get_object_or_404(Actor,pk=pk)
#     serializer=ActorSerializer(actor,data=request.data)
#     if serializer.is_valid(raise_exception=True):
#         serializer.save()
#         return Response(data=serializer.data, statu
#         s=status.HTTP_201_CREATED)


class ActorApi(APIView):
    def get(self,request):
        actors = Actor.objects.all()
        serialize=ActorSerializer(actors,many=True)
        return Response(data=serialize.data, status=status.HTTP_200_OK)
    
    def post(self,request):
        serialize=ActorSerializer(data=request.data)
        serialize.is_valid(raise_exception=True)
        serialize.save()
        return Response(data=serialize.data,status=status.HTTP_201_CREATED)
    

class ActorUpdate(APIView):
    def put(self,request,pk):
        actor=get_object_or_404(Actor,pk=pk)
        serializer=ActorSerializer(actor,data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)
    
    def patch(self,request,pk):
        actor=get_object_or_404(Actor,pk=pk)
        serializer=ActorSerializer(actor,data=request.data,partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)

    def delete(self,request,pk):
        actor=get_object_or_404(Actor,pk=pk)
        actor.delete()
        return Response(data={'message':'Deleted'},status=status.HTTP_204_NO_CONTENT)
    
class MovieApi(APIView):
    def get(self,request):
        movies=Movie.objects.all()
        serialize=MovieSerializer(movies,many=True)
        return Response(data=serialize.data,status=status.HTTP_200_OK)
    
    def post(self,request):
        serialize=MovieSerializer(data=request.data)
        serialize.is_valid(raise_exception=True)
        serialize.save()
        return Response(data=serialize.data,status=status.HTTP_201_CREATED)
    
class MovieUpdate(APIView):
    
    def put(self,request,pk):
        movie=get_object_or_404(Movie,pk=pk)
        serialize=MovieSerializer(movie,data=request.data)
        serialize.is_valid(raise_exception=True)
        serialize.save()
        return Response(data=serialize.data,status=status.HTTP_201_CREATED)
    
    def patch(self,request,pk):
        movie=get_object_or_404(Movie,pk=pk)
        serialize=MovieSerializer(movie,data=request.data,partial=True)
        serialize.is_valid(raise_exception=True)
        serialize.save()
        return Response(data=serialize.data,status=status.HTTP_201_CREATED)
    
    def delete(self,request,pk):
        movie=get_object_or_404(Movie,pk=pk)
        movie.delete()
        return Response(data={'message':'Deleted'},status=status.HTTP_204_NO_CONTENT)
    
class ActorsofMovie(APIView):
    def get(self,request):
        movie=Movie.objects.annotate(count_actor=Count('actor')).filter(count_actor__lt=3)
        serialize=MovieSerializer(movie,many=True)
        return Response(data=serialize.data, status=status.HTTP_200_OK)

    
class MoviesYear(ActorApi):
    def get(self,request,year1,year2=None):
        if year2 is not None:
            movie = Movie.objects.filter(year__range=(year1, year2))
        else:
            movie=Movie.objects.filter(year=year1)
        
        return Response(data=MovieSerializer(movie,many=True).data,status=status.HTTP_200_OK)

