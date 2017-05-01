from rest_framework import serializers
from ConcertifyApi.models import User, Musician, Location, Tag, Concert,MainHall

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ('name', 'username', 'location', 'favorite_musician')

class MusicianSerializer(serializers.ModelSerializer):
	class Meta:
		model = Musician
		fields = ('name', 'genre', 'tag')

class LocationSerializer(serializers.ModelSerializer):
	class Meta:
		model = Location
		fields = ('name', 'address', 'latitude', 'longtitude')

class TagSerializer(serializers.ModelSerializer):
	class Meta:
		model = Tag
		fields = ('tagID', 'text')

class ConcertSerializer(serializers.ModelSerializer):
	class Meta:
		model = Concert
		fields=('name','location','musician')

class MainHallSerializer(serializers.ModelSerializer):
	class Meta:
		model = MainHall
		fields = ('name', 'address', 'capacity')
