from django.shortcuts import render

from django.shortcuts import get_object_or_404
from django.http import Http404
from rest_framework.response import Response
from rest_framework.views import APIView
#----------------MODELOS----------------
from Profile.models import ProfileModel
#----------SERIELIZERS----------------
from Profile.serializers import ProfileModelSerializer
# -------------------View-----------------
class ProfileModelView(APIView):

    def post (self, request, format=None):
        serializer = ProfileModelSerializer(data= request.data, context = {'request': request})
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data)

       # response = ResponseJson("Eror")
        return Response("Error Formato") 