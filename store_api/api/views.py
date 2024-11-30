from django.shortcuts import render
from .models import Token, Good
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import TokenSerializer, GoodSerializer
from uuid import uuid4


class GetToken(APIView):
    def get(self, request):
        token = Token.objects.create(token=uuid4())
        token.save()
        data = TokenSerializer(token, many=False).data
        return Response(data, status=status.HTTP_201_CREATED)

class GetGood(APIView):
    def get(self, request):
        if not('token' in request.GET):
            return Response("Token must be presented", status=status.HTTP_400_BAD_REQUEST)
        token = request.GET['token']
        if not(Token.objects.filter(token=token).all()):
            return Response("Token is not valid", status=status.HTTP_401_UNAUTHORIZED)

        goods = Good.objects.all()
        data = GoodSerializer(goods, many=True).data

        return Response(data, status=status.HTTP_200_OK)

class AddGoods(APIView):
    def post(self, request):
        if not('token' in request.GET):
            return Response("Token must be presented", status=status.HTTP_400_BAD_REQUEST)
        token = request.GET['token']
        if not(Token.objects.filter(token=token).all()):
            return Response("Token is not valid", status=status.HTTP_401_UNAUTHORIZED)

        data = request.data
        data = GoodSerializer(data=data)
        if data.is_valid():
            data.create(data.validated_data)
            return Response(data=data.data, status=status.HTTP_201_CREATED)
        return Response(data=data.errors, status=status.HTTP_400_BAD_REQUEST)
# Token.objects.create().save()

# Create your views here.
