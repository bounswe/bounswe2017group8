# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from ConcertifyApi.models import User, Musician, Location, Tag
from ConcertifyApi.serializers import UserSerializer, MusicianSerializer, LocationSerializer, TagSerializer 
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404

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
                    print("Existing name, send error.")
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserList(APIView):
    def get(self, request, format=None):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            users = User.objects.all()
            for user in users:
                if user.username == serializer.validated_data.get('username'):
                    print("Existing username, send error.")
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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
                    print("Existing address, send error.")
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
                    print("Existing tag, send error.")
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
