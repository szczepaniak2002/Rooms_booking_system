from django.contrib import admin

# Register your models here.
from .models import Location, Room, Reservation

admin.site.register(Location)
admin.site.register(Room)
admin.site.register(Reservation)