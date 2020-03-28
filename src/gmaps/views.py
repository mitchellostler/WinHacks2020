from django.shortcuts import render
from .models import address
import requests
# Create your views here.



def get_maps_image(address):
    mapskey='AIzaSyB9T3n9WYiZKyr139VKRMIZTZI2speuavI'
    url = "https://maps.googleapis.com/maps/api/staticmap?"
    # center defines the center of the map, 
    # equidistant from all edges of the map.  
    center = 'center={},{}'.format(address.coord['lat'], address.coord['long'])
    # zoom defines the zoom 
    # level of the map 
    zoom = '&zoom={}'.format('10')
    user_marker = '&markers=color:red%7Clabel:C%7C{}}'.format(address.coord['lat'], address.coord['long'])
    # get method of requests module 
    # return response object 
    google_url = url + center + zoom + "&size=400x400&key=" + mapskey
    print(google_url)
    r = requests.get(url + center + zoom + "&size=400x400&key=" + mapskey) 
    #up until here is working

    #TODO: find way to store image and get to front end
    # wb mode is stand for write binary mode 
    f = open('map.png', 'wb') 
    f.write(r.content) 
    f.close() 
