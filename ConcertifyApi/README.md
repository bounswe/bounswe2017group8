# Concertify API

Python - Django REST framework is used and to obtain the development environment the following page may be checked: http://www.django-rest-framework.org/#installation

## **Quick Tutorial:**  
**1.** Install Python
 - On Windows and Mac, download from [here](https://www.python.org/downloads) and do not forget the check **Add Python to environment variables** for Windows (Default is unchecked)
 
 - For other platforms : Check [here](https://docs.python.org/3/using/unix.html).


From command-line,  
**2.** `pip install django`  
**3.** `pip install djangorestframework`  
<br/>
**4.** Download the bounswe/bounswe2017group8 repository([Shortcut](https://github.com/bounswe/bounswe2017group8/archive/master.zip))  
**5.** Extract the zip file to X folder

From command-line,  
**6.** `cd (Path of X)/bounswe2017group8/ConcertifyApi`  
<br/>
 The next command shall run the project as a local server:  
**7.** `python manage.py runserver`  
Now, API is accessible via http://127.0.0.1:8000/. Data shall be in JSON format.  
_GET_ , _POST_ and  requests are available for those classes:
* **User** ('name', 'username', 'location', 'favorite_musician') ( _DELETE_ request is also available)

| Key               | Value Type | Value Description                    |
| ----------------- | ---------- | ------------------------------------ |
| name              | string     | Name of the user                     |
| username          | string     | Login name of the user               |
| location          | string     | Location of the user                 |
| favorite_musician | string     | Name of the user's favorite musician |

* **Musician** ('name', 'genre', 'tag')

| Key        | Value Type | Value Description                           |
| ---------- | ---------- | ------------------------------------------- |
| name       | string     | Name of the Musician                        |
| genre      | string     | Genre of the Musician in which they perform |
| tag        | string     | Related tags for this Musician              |

* **Location** ('name', 'address', 'latitude', 'longtitude')

| Key        | Value Type | Value Description            |
| ---------- | ---------- | ---------------------------- |
| name       | string     | Name of the location         |
| address    | string     | Open address of the location |
| latitude   | float      | Latitude of the address      |
| longtitude | float      | Longtitude of the address    |

* **Tag** ('tagID', 'text')

| Key      | Value Type | Value Description         |
| -------- | ---------- | ------------------------- |
| tagID    | int        | ID of the tag             |
| text     | string     | The text value of the tag |

* **Concert** ('name','location','musician')

| Key        | Value Type | Value Description                           |
| ---------- | ---------- | ------------------------------------------- |
| name       | string     | Name of the event                           |
| location   | string     | Location of the user                        |
| musician   | string     | List of musicians taking place in the event |

* **MainHall** ('name', 'address', 'capacity')

| Key      | Value Type | Value Description        |
| -------- |----------- | ------------------------ |
| name     | string     | Name of the main hall    |
| address  | string     | Open address of the hall |
| capacity | int        | Spectator capacity       |

* **Comment** ('commentID', 'commentOwner', 'content', 'voteCount')

| Key         | Value Type | Value Description                             |
| ----------- | ---------- | --------------------------------------------- |
| commentID   | int        | ID number of the Comment                      |
| commentOwner| string     | The User who has written this Comment         |
| content     | string     | The text content of this Content              |
| voteCount   | int        | Number of users who has voted this Comment up |


You may use Postman program to make _GET_ , _POST_ and _DELETE_ requests.  
**8.** Install Postman ([Shortcut](https://www.getpostman.com/))  
**9.** You shall need an account to post data to http://127.0.0.1:8000/. Enter the credentials (admin:test1234) as `Basic Auth` under Authorization tab.

## **Unit Tests:**  
In order to run available unit tests,  
From command-line,  
`cd (Path of X)/bounswe2017group8/ConcertifyApi`  
and then `python manage.py test`  

Existing unit test classes and their corresponding test methods are:  
  
**1. UserTestCase**
* test_list_users
* test_delete_user
* test_create_new_user
* test_create_existing_user

**2. MusicianTestCase**
* test_list_musicians

**3. LocationTestCase**
* test_list_location

**4. ConcertTestCase**
* test_list_concert

**5. MainHallTestCase**
* test_list_mainhall

## **Endpoint Reference:**

Web API Base URL: http://52.59.27.221

|Method|Endpoint|Usage|Returns|Auth|
|------|--------|-----|-------|----|
|GET|/mainhalls|Get features of all recorded main event halls|Array of MainHall objects (JSON)| |
|POST|/mainhalls/|Save a MainHall object|HTTP_201:Currently saved MainHall object features  HTTP_400:Bad request|Basic Auth|
|GET|/tags|Get features of all recorded tags|Array of Tag objects (JSON)| |
|POST|/tags/|Save a Tag object|HTTP_201:Currently saved Tag object features  HTTP_400:Bad request|Basic Auth|
|GET|/locations|Get features of all recorded locations|Array of Location objects (JSON)| |
|POST|/locations/|Save a Location object|HTTP_201:Currently saved Location object features  HTTP_400:Bad request|Basic Auth|
|GET|/users|Get features of all recorded users|Array of User objects (JSON)| |
|POST|/users/|Save a User object|HTTP_201:Currently saved User object features  HTTP_400:Bad request|Basic Auth|
