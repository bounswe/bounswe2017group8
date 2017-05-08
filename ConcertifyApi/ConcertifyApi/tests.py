# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

import requests
from requests.auth import HTTPBasicAuth

from ConcertifyApi.models import User

class UserTestCase(TestCase):
    # Test the functionality of listing users
    def test_list_users(self):
        # Make a request to list users
        list_response = requests.get('http://127.0.0.1:8000/users', auth=HTTPBasicAuth('admin', 'test1234'))

        # Check if the status code of the was a success
        self.assertEqual(list_response.status_code // 100, 2, 'HTTP request response indicates an error code.')

        # Check if the dummy user is found and its information is correct
        found = False
        for user_data in list_response.json():
            if user_data['username'] == 'dummy':
                found = True
                # Assert that the user info is correct
                self.assertEqual(user_data['name'], 'Dummy User', 'Dummy user is found, but the name is wrong.')
                self.assertEqual(user_data['location'], 'Dummistan', 'Dummy user is found, but the location is wrong.')
                self.assertEqual(user_data['favorite_musician'], 'Rolling Dummies', 'Dummy user is found, but the favorite musician is wrong.')

        # Assert that the dummy user is found
        self.assertTrue(found, 'Dummy user could not be found.')

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

        create_response = requests.post('http://127.0.0.1:8000/users/', auth=HTTPBasicAuth('admin', 'test1234'), data = user_info)

        self.assertEqual(create_response.status_code // 100, 4, 'Creating an existing user should return a bad request error: {}'.format(create_response.status_code))