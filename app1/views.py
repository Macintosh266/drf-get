from django.db.models import *
from django.template.defaulttags import comment
from rest_framework.permissions import IsAuthenticated
from .serializers import *
from django.shortcuts import render,get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import *
import json
from drf_yasg.utils import swagger_auto_schema





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
    
    @swagger_auto_schema(request_body=ActorSerializer,)
    def post(self,request):
        serialize=ActorSerializer(data=request.data)
        serialize.is_valid(raise_exception=True)
        serialize.save()
        return Response(data=serialize.data,status=status.HTTP_201_CREATED)
    

class ActorUpdate(APIView):
    @swagger_auto_schema(request_body=ActorSerializer,)
    def put(self,request,pk):
        actor=get_object_or_404(Actor,pk=pk)
        serializer=ActorSerializer(actor,data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)
    
    @swagger_auto_schema(request_body=ActorSerializer,)
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
    
    @swagger_auto_schema(request_body=MovieSerializer,)
    def post(self,request):
        serialize=MovieSerializer(data=request.data)
        serialize.is_valid(raise_exception=True)
        serialize.save()
        return Response(data=serialize.data,status=status.HTTP_201_CREATED)
    
class MovieUpdate(APIView):
    @swagger_auto_schema(request_body=MovieSerializer,)
    def put(self,request,pk):
        movie=get_object_or_404(Movie,pk=pk)
        serialize=MovieSerializer(movie,data=request.data)
        serialize.is_valid(raise_exception=True)
        serialize.save()
        return Response(data=serialize.data,status=status.HTTP_201_CREATED)
    
    @swagger_auto_schema(request_body=MovieSerializer,)
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

    
class MoviesYear(APIView):
    def get(self,request,year1,year2=None):
        if year2 is not None:
            movie = Movie.objects.filter(year__range=(year1, year2))
        else:
            movie=Movie.objects.filter(year=year1)
        
        return Response(data=MovieSerializer(movie,many=True).data,status=status.HTTP_200_OK)



class CommentListCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        comments = CommitMovie.objects.filter(author=request.user)
        serializer = CommentSerializer(comments, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=CommentSerializer)
    def post(self, request):
        response={'success':True}
        serializer = CommentSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save(author=request.user)
            response['date']=serializer.data
            return Response(data=response, status=status.HTTP_201_CREATED)
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)


class CommentDetailView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, pk):
        comment = get_object_or_404(CommitMovie, pk=pk)
        serializer = CommentSerializer(comment)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=CommentSerializer)
    def put(self, request, pk):
        response={'success':True}
        comment = get_object_or_404(CommitMovie, pk=pk)
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(author=request.user)
            response['date']=serializer.data
            return Response(data=response, status=status.HTTP_201_CREATED)
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)

    @swagger_auto_schema(request_body=CommentSerializer)
    def patch(self, request, pk):
        response={'success':True}
        comment = get_object_or_404(CommitMovie, pk=pk)
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(author=request.user)
            response['date']=serializer.data
            return Response(data=response, status=status.HTTP_201_CREATED)
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)

    def delete(self, request, pk):
        comment = get_object_or_404(CommitMovie, pk=pk)
        comment.delete()
        return Response(data={'message': 'Deleted'}, status=status.HTTP_204_NO_CONTENT)