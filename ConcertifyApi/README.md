# Concertify API

Python - Django REST framework is used and to obtain the development environment the following page may be checked: http://www.django-rest-framework.org/#installation

## **Quick Tutorial:**  
**1.** Install Python
 - On Windows, download from https://www.python.org/downloads and do not forget the check **Add Python to environment variables** (Default is unchecked)  
 - On Linux, Mac: `pip install django`  

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
_GET_ , _POST_ and _DELETE_ requests are available for those classes:
* **User** ('name', 'username', 'location', 'favorite_musician')
* **Musician** ('name', 'genre', 'tag')
* **Location** ('name', 'address', 'latitude', 'longtitude')
* **Tag** ('tagID', 'text')
* **Concert** ('name','location','musician')
* **MainHall** ('name', 'address', 'capacity')
* **Comment** ('commentID', 'commentOwner', 'content', 'voteCount')


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

## **Enpoint Reference**
|Method|Endpoint|Usage|Returns|
|------|--------|-----|-------|
|GET||||
|POST||||
