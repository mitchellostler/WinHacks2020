from django.db import models
import googlemaps
maps_key = 'AIzaSyB9T3n9WYiZKyr139VKRMIZTZI2speuavI'
gmaps = googlemaps.Client(key=maps_key)
# Geocoding an address

# Create your models here.


class address(models.Model):
    street_ad = models.CharField(max_length=220)

    lat = models.DecimalField(max_digits=12, decimal_places=6, default=0)
    long = models.DecimalField(max_digits=12, decimal_places=6, default=0)

    def street_to_coord(self):
        geocode_results = gmaps.geocode(self.street_ad)
        self.lat = geocode_results[0]['geometry']['location']['lat']
        self.long = geocode_results[0]['geometry']['location']['lng']
        # if the address can not be found function will return false
        if geocode_results == []:
            return False
        return True


class drive_route(models.Model):
    dist_km = models.DecimalField(max_digits=3, decimal_places=2, default=0)
    time_it = models.CharField(max_length=30)

    def get_distance_km(self, origin, dest):
        base = 'https://maps.googleapis.com/maps/api/distancematrix/json?units=metric'
        orgString = '&origins={},{}'.format(
            str(self.origin.coord['lat']), str(self.origin.coord['long']))
        dstString = '&destinations={},{}'.format(
            self.dest.coord['lat'], self.dest.coord['long'])
        drv_req_url = base + orgString + dstString + '&key=' + maps_key
        print(drv_req_url)

