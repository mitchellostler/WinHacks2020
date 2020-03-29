from django.contrib import admin

# Register your models here.


# importing the models

from .models import *


admin.site.register(Donator)
admin.site.register(Item)
admin.site.register(Tag)
admin.site.register(Donate)
