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
    # Define the GET method for listing users
    def get(self, request, format=None):
        # Get all the users and create a serializer for them
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)

        # Add id data to the serializer
        for user in serializer.data:
            user['pk'] = User.objects.get(username=user['username']).pk

        # Return serializer content
        return Response(serializer.data)

    # Define POST method for creating a new user
    def post(self, request, format=None):
        # Create a new user serializer with given data
        serializer = UserSerializer(data=request.data)

        # If given data is valid save new user
        if serializer.is_valid():
            users = User.objects.all()

            # Check if there exists a user with the same username
            for user in users:
                if user.username == serializer.validated_data.get('username'):
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            # All is OK
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        # If data is invalid return BAD REQUEST
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


"""
List all musicians or create a new musician.
"""
class MusicianList(APIView):
    # Define the GET method for listing users
    def get(self, request, format=None):
        # Get all the users and create a serializer for them
        musicians = Musician.objects.all()
        serializer = MusicianSerializer(musicians, many=True)

        # Add id data to the serializer
        for musician in serializer.data:
            musician['pk'] = Musician.objects.filter(name=musician['name'])[0].pk

        # Return serializer content
        return Response(serializer.data)

    # Define POST method for creating a new musician
    def post(self, request, format=None):
        # Create a new musician serializer with given data
        serializer = MusicianSerializer(data=request.data)

        # If given data is valid save new musician
        if serializer.is_valid():
            serializer.save()

            # All is OK
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        # If data is invalid return BAD REQUEST
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MusicianDetail(APIView):
    def get_object(self, pk):
        try:
            return Musician.objects.get(pk=pk)
        except Musician.DoesNotExist:
            raise Http404

    # Return information of a specific musician
    def get(self, request, pk, format=None):
        musician = self.get_object(pk)
        serializer = MusicianSerializeru(musician)
        return Response(serializer.data)

    # Modify a musician
    def put(self, request, pk, format=None):
        musician = self.get_object(pk)
        serializer = MusicianSerializer(musician, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Delete a musician
    def delete(self, request, pk, format=None):
        musician = self.get_object(pk)
        musician.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

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

class LocationDetail(APIView):
    def get_object(self, pk):
        try:
            return Location.objects.get(pk=pk)
        except Location.DoesNotExist:
            raise Http404

    # Return information of a specific location
    def get(self, request, pk, format=None):
        location = self.get_object(pk)
        serializer = LocationSerializer(location)
        return Response(serializer.data)

    # Modify a location
    def put(self, request, pk, format=None):
        location = self.get_object(pk)
        serializer = LocationSerializer(location, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Delete a location
    def delete(self, request, pk, format=None):
        location = self.get_object(pk)
        location.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


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
