# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

import requests
from requests.auth import HTTPBasicAuth

from ConcertifyApi.models import User

"""
Test cases for the User class
"""
class UserTestCase(TestCase):
    # Test the functionality of listing users
    def test_list_users(self):
        user_info = {'username': 'list_temp_dummy', 'name': 'Temporary Dummy User', 'location': 'Dummistan', 'favorite_musician': 'Rolling Dummies'}

        create_response = requests.post('http://127.0.0.1:8000/users/', auth=HTTPBasicAuth('admin', 'test1234'), data = user_info)

        # Make a request to list users
        list_response = requests.get('http://127.0.0.1:8000/users', auth=HTTPBasicAuth('admin', 'test1234'))

        # Check if the status code of the was a success
        self.assertEqual(list_response.status_code // 100, 2, 'HTTP request response indicates an error code.')

        # Check if the dummy user is found and its information is correct
        found = False
        for user_data in list_response.json():
            if user_data['username'] == 'list_temp_dummy':
                found = True
                # Assert that the user info is correct
                self.assertEqual(user_data['name'], 'Temporary Dummy User', 'Dummy user is found, but the name is wrong.')
                self.assertEqual(user_data['location'], 'Dummistan', 'Dummy user is found, but the location is wrong.')
                self.assertEqual(user_data['favorite_musician'], 'Rolling Dummies', 'Dummy user is found, but the favorite musician is wrong.')

        # Assert that the dummy user is found
        self.assertTrue(found, 'Dummy user could not be found.')

        # Cleanup the dummy user data
        search_pk = 0
        for user_data in list_response.json():
            if user_data['username'] == 'list_temp_dummy':
                search_pk = user_data['pk']

        delete_url = 'http://127.0.0.1:8000/users/' + str(search_pk) + '/'
        requests.delete(delete_url, auth=HTTPBasicAuth('admin', 'test1234'))

    def test_delete_user(self):
        user_info = {'username': 'delete_temp_dummy', 'name': 'Temporary Dummy User', 'location': 'Dummistan', 'favorite_musician': 'Rolling Dummies'}

        create_response = requests.post('http://127.0.0.1:8000/users/', auth=HTTPBasicAuth('admin', 'test1234'), data = user_info)
        list_response = requests.get('http://127.0.0.1:8000/users/', auth=HTTPBasicAuth('admin', 'test1234'))

        self.assertEqual(list_response.status_code // 100, 2, 'Error creating a temporary user.')

        search_pk = 0
        for user_data in list_response.json():
            if user_data['username'] == 'delete_temp_dummy':
                search_pk = user_data['pk']

        delete_url = 'http://127.0.0.1:8000/users/' + str(search_pk) + '/'
        requests.delete(delete_url, auth=HTTPBasicAuth('admin', 'test1234'), data = user_info)

        list_response = requests.get('http://127.0.0.1:8000/users/', auth=HTTPBasicAuth('admin', 'test1234'))

        found = False
        for user_data in list_response.json():
            if user_data['username'] == 'delete_temp_dummy':
                found = True

        self.assertFalse(found, 'Error deleting the temporary user.')

    def test_create_new_user(self):
        user_info = {'username': 'create_temp_dummy', 'name': 'Temporary Dummy User', 'location': 'Dummistan', 'favorite_musician': 'Rolling Dummies'}

        create_response = requests.post('http://127.0.0.1:8000/users/', auth=HTTPBasicAuth('admin', 'test1234'), data = user_info)

        self.assertEqual(create_response.status_code // 100, 2, 'HTTP request response indicates an error code: {}'.format(create_response.status_code))

        list_response = requests.get('http://127.0.0.1:8000/users', auth=HTTPBasicAuth('admin', 'test1234'))

        # Check if the dummy user is found and its information is correct
        found = False
        for user_data in list_response.json():
            if user_data['username'] == 'create_temp_dummy':
                found = True
                # Assert that the user info is correct
                self.assertEqual(user_data['name'], 'Temporary Dummy User', 'New user is found, but the name is wrong.')
                self.assertEqual(user_data['location'], 'Dummistan', 'New user is found, but the location is wrong.')
                self.assertEqual(user_data['favorite_musician'], 'Rolling Dummies', 'New user is found, but the favorite musician is wrong.')

        # Assert that the dummy user is found
        self.assertTrue(found, 'New dummy user could not be created.')

        search_pk = 0
        for user_data in list_response.json():
            if user_data['username'] == 'create_temp_dummy':
                search_pk = user_data['pk']

        list_response = requests.get('http://127.0.0.1:8000/users', auth=HTTPBasicAuth('admin', 'test1234'))

        delete_url = 'http://127.0.0.1:8000/users/' + str(search_pk) + '/'
        requests.delete(delete_url, auth=HTTPBasicAuth('admin', 'test1234'), data = user_info)

    def test_create_existing_user(self):
        user_info = {'username': 'dummy', 'name': 'Dummy User', 'location': 'Dummistan', 'favorite_musician': 'Rolling Dummies'}

        create_response_1 = requests.post('http://127.0.0.1:8000/users/', auth=HTTPBasicAuth('admin', 'test1234'), data = user_info)
        create_response_2 = requests.post('http://127.0.0.1:8000/users/', auth=HTTPBasicAuth('admin', 'test1234'), data = user_info)

        self.assertEqual(create_response_2.status_code // 100, 4, 'Creating an existing user should return a bad request error: {}'.format(create_response_2.status_code))

        list_response = requests.get('http://127.0.0.1:8000/users/', auth=HTTPBasicAuth('admin', 'test1234'))

        # Cleanup the dummy user data
        search_pk = 0
        for user_data in list_response.json():
            if user_data['username'] == 'dummy':
                search_pk = user_data['pk']

        delete_url = 'http://127.0.0.1:8000/users/' + str(search_pk) + '/'
        requests.delete(delete_url, auth=HTTPBasicAuth('admin', 'test1234'))

"""
Test cases for the Musician class
"""
class MusicianTestCase(TestCase):
    # Test the functionality of listing musicians
    def test_list_musicians(self):
        musician_info = {'name': 'Dummy Musician', 'genre': 'Dummy Genre', 'tag': 'Dummy Tag'}
        create_response = requests.post('http://127.0.0.1:8000/musicians/', auth=HTTPBasicAuth('admin', 'test1234'), data = musician_info)

        # Make a request to list musicians
        list_response = requests.get('http://127.0.0.1:8000/musicians', auth=HTTPBasicAuth('admin', 'test1234'))

        # Check if the status code of the was a success
        self.assertEqual(list_response.status_code // 100, 2, 'HTTP request response indicates an error code.')

        # Check if the dummy usemusician is found and its information is correct
        found = False
        for musician_data in list_response.json():
            if musician_data['name'] == musician_info['name']:
                found = True
                # Assert that the user info is correct
                self.assertEqual(musician_data['genre'], musician_info['genre'], 'Dummy musician is found, but the genre is wrong.')
                self.assertEqual(musician_data['tag'], musician_info['tag'], 'Dummy musician is found, but the tag is wrong.')

        # Assert that the dummy user is found
        self.assertTrue(found, 'Dummy musician could not be found.')

        search_pk = 0
        for musician_data in list_response.json():
            if musician_data['name'] == 'Dummy Musician':
                search_pk = musician_data['pk']

        delete_url = 'http://127.0.0.1:8000/musicians/' + str(search_pk) + '/'
        requests.delete(delete_url, auth=HTTPBasicAuth('admin', 'test1234'))

"""
Test cases for the Location class
"""
class LocationTestCase(TestCase):
    # Test the functionality of listing locations
    def test_list_location(self):
        # Make a request to list locations
        list_response = requests.get('http://127.0.0.1:8000/locations/', auth=HTTPBasicAuth('admin', 'test1234'))

        # Check if the status code of the was a success
        self.assertEqual(list_response.status_code // 100, 2, 'HTTP request response indicates an error code.')

"""
Test cases for the Concert class
"""
class ConcertTestCase(TestCase):
    # Test the functionality of listing concerts
    def test_list_concert(self):
        # Make a request to list concerts
        list_response = requests.get('http://127.0.0.1:8000/concerts/', auth=HTTPBasicAuth('admin', 'test1234'))

        # Check if the status code of the was a success
        self.assertEqual(list_response.status_code // 100, 2, 'HTTP request response indicates an error code.')

"""
Test cases for the Main Hall class
"""
class MainHallTestCase(TestCase):
    # Test the functionality of listing main halls
    def test_list_mainhall(self):
        # Make a request to list main halls
        list_response = requests.get('http://127.0.0.1:8000/mainhalls/', auth=HTTPBasicAuth('admin', 'test1234'))

        # Check if the status code of the was a success
        self.assertEqual(list_response.status_code // 100, 2, 'HTTP request response indicates an error code.')

