# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from ConcertifyApi.models import User, Musician, Location, Tag, Concert, MainHall
from ConcertifyApi.serializers import UserSerializer, MusicianSerializer, LocationSerializer, TagSerializer, ConcertSerializer, MainHallSerializer

from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404

"""
List all users or create a new user.
"""
class UserList(APIView):
    def get(self, request, format=None):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)

        for user in serializer.data:
            user['pk'] = users = User.objects.get(username=user['username']).pk
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            users = User.objects.all()
            for user in users:
                if user.username == serializer.validated_data.get('username'):
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

"""
View, update or delete a single user.
"""
class UserDetail(APIView):
    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        user = self.get_object(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class MusicianList(APIView):
    def get(self, request, format=None):
        musicians = Musician.objects.all()
        serializer = MusicianSerializer(musicians, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = MusicianSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LocationList(APIView):
    def get(self, request, format=None):
        locations = Location.objects.all()
        serializer = LocationSerializer(locations, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = LocationSerializer(data=request.data)
        if serializer.is_valid():
            locations = Location.objects.all()
            for location in locations:
                if location.address == serializer.validated_data.get('address'):
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TagList(APIView):
    def get(self, request, format=None):
        tags = Tag.objects.all()
        serializer = TagSerializer(tags, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = TagSerializer(data=request.data)
        if serializer.is_valid():
            tags = Tag.objects.all()
            for tag in tags:
                if tag.text == serializer.validated_data.get('text'):
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ConcertList(APIView):
    def get(self,request,format=None):
        concerts=Concert.objects.all()
        serializer=ConcertSerializer(concerts, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ConcertSerializer(data=request.data)
        if serializer.is_valid():
            concert = Concert.objects.all()
            for concert in concerts:
                if concert.name == serializer.validated_data.get('name'):
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MainHallList(APIView):
    def get(self, request, format=None):
        mainHalls = MainHall.objects.all()
        serializer = MainHallSerializer(mainHalls, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = MainHallSerializer(data=request.data)
        if serializer.is_valid():
            mainHalls = MainHall.objects.all()
            for mainHall in mainHalls:
                if mainHall.name == serializer.validated_data.get('name'):
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
