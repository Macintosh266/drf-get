from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
import json


class Hello(APIView):
    def get(self,request):
        context={
            'salom':'dunyo'
        }
        with open('data.json','r') as json_file:
            data=json.load(json_file)
            print(data)

        return Response(data=data)

    def post(self,request):
        name=request.data["name"]
        phone=request.data["phone"]
        email=request.data["email"]
        context={
            "respose":f"salom  {name}",
            "reponse1":f" telefon: {phone}",
            "reponse2":f"email: {email}"
        }
        # with open('data.json','r') as json_file:
        #     data=json_file

        return Response(data=context)
