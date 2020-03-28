from django.db import models
import googlemaps
gmaps = googlemaps.Client(key='AIzaSyB9T3n9WYiZKyr139VKRMIZTZI2speuavI')
# Geocoding an address

# Create your models here.

class address(models.Model):
    street_ad = models.CharField(max_length = 220)
    coord = {
        'lat' : models.DecimalField(max_digits=None),
        'long' : models.DecimalField(max_digits=None)
    }
    def street_to_coord(self):
        geocode_results = gmaps.geocode(self.street_ad)
        self.coord['lat'] = geocode_results[0]['geometry']['location']['lat']
        self.coord['long'] = geocode_results[0]['geometry']['location']['lng']
        #if the address can not be found function will return false
        if geocode_results == []: 
            return False
        return True




