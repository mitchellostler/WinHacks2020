from django.shortcuts import render
from .models import address
import requests
# Create your views here.



def get_maps_image():
    
    mapskey='AIzaSyB9T3n9WYiZKyr139VKRMIZTZI2speuavI'
    url = "https://maps.googleapis.com/maps/api/staticmap?"
    # center defines the center of the map, 
    # equidistant from all edges of the map.  

    center = 'center={},{}'.format(45.274912, -75.9129349)
    
    # zoom defines the zoom 
    # level of the map 
    #user_marker = '&markers=color:red%7Clabel:C%7C{}}'.format(45.274912, -75.9129349)
    # get method of requests module 
    # return response object 
    #google_url = url + center + "&size=400x400&key=" + mapskey
    defaulturl = '''https://maps.googleapis.com/maps/api/staticmap?
    center=Brooklyn+Bridge,New+York,NY&zoom=13&size=600x300&maptype=roadmap
    &markers=color:blue%7Clabel:S%7C40.702147,-74.015794
    &markers=color:blue%7Clabel:G%7C40.711614,-74.012318
    &markers=color:red%7Clabel:C%7C40.718217,-73.998284
    &key={}'''.format(mapskey)   
    print(defaulturl)
    r = requests.get(defaulturl) 
    #up until here is working
    return r
