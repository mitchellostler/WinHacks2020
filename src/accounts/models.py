from django.db import models

# Create your models here.


# Creating a Donator table

class Donator(models.Model):
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    # To be able to view the string value of the donator

    def __str__(self):
        return self.name

# the item's tag


class Tag(models.Model):
    name = models.CharField(max_length=200, null=True)

    # To be able to view the string value of the donator

    def __str__(self):
        return self.name


class Item(models.Model):

    CATEGORY = (
        ('Food', 'Food'),
        ('medical', 'medical'),
        ('home', 'home'),
        ('misc', 'misc'),
    )

    name = models.CharField(max_length=200, null=True)
    category = models.CharField(max_length=200, null=True, choices=CATEGORY)
    description = models.CharField(max_length=200, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.name


class Donate(models.Model):

    # creating a tuple that contains different types/values to assign to status of the item

    STATUS = (

        ('Pending', 'Pending'),
        ('Out for delivery', 'Out for delivery'),
        ('Delivered', 'Delivered'),



    )

    # on_delete allows us not to delete the donators donation
    donator = models.ForeignKey(Donator, null=True, on_delete=models.SET_NULL)
    item = models.ForeignKey(Item, null=True, on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=200, null=True, choices=STATUS)

