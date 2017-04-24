from rest_framework import serializers
from ConcertifyApi.models import User, Musician, Location, Tag

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
		fields = ('ID', 'text')