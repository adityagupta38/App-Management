#DRF test  Apps api application
#give appropriate app id(pk) to perform CRUD operations on it wherever id parameter is required
#for getting resource authenticating credentials is not required.
# for Performing Create,Update,Delete Operations Authenticating credentials username & password is required everytime.
# Admin Username and Password is required for Apps api CRUD functions.
# get method & get method with id is used to fetch app list and app detail respectively.
# Post verb is used for Creating app
# put verb is used for updating app
# patch verb is used for partial update of app resource
# delete verb is used for deleting app

import requests
import json

BASE_URL='http://127.0.0.1:8000/'    # give here your localhost ipaddress and port No
ENDPOINT='apps/'
username='adityagupta'  #registered admin username
password='1234'         #admin password

def get_apps_list():
    resp=requests.get(BASE_URL+ENDPOINT)
    print(resp.text)


def get_app_detail(id):
    resp=requests.get(BASE_URL+ENDPOINT+str(id)+'/')
    print(resp.text)


def create_app():
    img=open(r"C:\Users\adity\Downloads\naukri.webp",'rb')
    data={
        'username':username,
        'password':password,
        'app_name':'naukri.com',
        'app_link':'https://play.google.com/store/apps/details?id=naukriApp.appModules.login&gl=us',
        'app_category':'Jobs & Business',
        'app_subcategory':'Networking',
        'points':150,
        }
    resp=requests.post(BASE_URL+ENDPOINT, data=data,json=json, files={"app_image":img})
    img.close()
    print(resp.text)
        
def update_app(id):
    img=open(r"C:\Users\adity\Downloads\naukri.webp",'rb')
    data={
        'username':username,
        'password':password,
        'app_name':'naukri.com',
        'app_link':'https://play.google.com/store/apps/details?id=naukriApp.appModules.login&gl=us',
        'app_category':'Jobs & Business',
        'app_subcategory':'Networking',
        'points':100,
        }
    resp=requests.put(BASE_URL+ENDPOINT+str(id)+'/', data=data,json=json, files={"app_image":img})
    img.close()
    print(resp.text)

def partial_update_app(id):
    data={
        'username':username,
        'password':password,
        'points':150,
        }
    resp=requests.patch(BASE_URL+ENDPOINT+str(id)+'/', data=data,json=json)
    print(resp.text)


def delete_app(id):
    data={
        'username':username,
        'password':password,
        }
    resp=requests.delete(BASE_URL+ENDPOINT+str(id)+'/', data=data,json=json)
    print(resp.text)


get_app_list()
    
