from django.shortcuts import render,HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import  CreateAPIView
from .serializer import *
from API.models import *
from rest_framework_simplejwt.tokens import RefreshToken
# Create your views here.


def home(request):
    return HttpResponse("<h1>hellow Welcomne to my api</h1>")

# get refresh token if user is valid .
# u can store it in local storage and validate each time the user visite the website
# using Validate Function at line number 36:
class ObtainAuthTokenView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        try:
            # Check if the user exists in the User model
            user = CODERS.objects.get(UserName=username)
        except:
            return Response({'error': 'Invalid credentials'})

        if user.PassWord==password:
            refresh = RefreshToken.for_user(user)
            token = {
                'refresh': str(refresh)}
            return Response({'token': token})
        else:
            return Response({'error': 'Invalid credentials'})


class ValidateTokien(APIView):
    def post(self,request):
        token=request.data.get('token')

        try:
            refresh=RefreshToken(token)
            refresh.access_token.verify()
            userId=refresh.access_token.payload.get('user_id')

            return  Response({"valid":True,"userId":userId})
        except :
            return Response({"valid": False})


class CreateCoder(CreateAPIView):
    model=CODERS
    queryset = CODERS.objects.all()
    serializer_class = CoderSerializer