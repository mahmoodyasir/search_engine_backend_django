from django.shortcuts import render
from rest_framework import generics, mixins, viewsets, views, status
from rest_framework.response import Response


from django.http import JsonResponse
from django.http import HttpResponse
from django.views.generic import View
from django.views.generic import ListView
from .models import *

from .serializers import *
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import IsAdminUser
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from django.contrib.auth.models import User
import json


class DataListView(viewsets.ViewSet):
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [IsAuthenticated, ]
    def list(self, request):
        query = EveryData.objects.all().order_by("-id")
        serializers = EveryDataSerializer(query, many=True)
        return Response(serializers.data)


class SearchRecordView(viewsets.ViewSet):
    # authentication_classes = [TokenAuthentication, ]
    # permission_classes = [IsAuthenticated, ]
    def list(self, request):
        query = SearchRecord.objects.all().order_by("id")
        serializers = SearchRecordSerializer(query, many=True)
        return Response(serializers.data)


class RegisterView(views.APIView):
    def post(self, request):
        serializers = UserSerializer(data=request.data)

        if serializers.is_valid():
            serializers.save()
            return Response({"error": False, "message": f"User is created for '{serializers.data['username']}'"})
        return Response({"error": True, "message": "Something is wrong"})


class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        if user.is_staff:
            token, created = Token.objects.get_or_create(user=user)
            return Response({
                'admin_token': token.key,
                'user_id': user.pk,
                'email': user.email,
                "message": True
            })
        else:
            return Response({"error": True, "message": False})


class SearchRecordInput(views.APIView):
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [IsAuthenticated, ]

    def post(self, request):
        try:
            user = request.user
            data = request.data
            every_data_id = EveryData.objects.get(id=data["s_id"])
            count = every_data_id.search_count
            every_data_id.search_count = count + 1
            print(every_data_id.search_count)
            print(user)
            print(data["s_id"])
            print(data["s_value"])

            SearchRecord.objects.create(
                user_id=user,
                search_id=data["s_id"],
                search_value=data["s_value"],
            )
            every_data_id.save()
            response_msg = {"error": False, "message": "User Data is Updated"}
        except:
            response_msg = {"error": True, "message": "User Data is not update !! Try Again ...."}
        return Response(response_msg)

