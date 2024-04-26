from django.db import models
from django.contrib.auth.models import User


ROOM_STATUS = (
    ("available","1"),
    ("not available","2"),
)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
class Location(models.Model):
    address = models.CharField(max_length=100,primary_key=True)
    city = models.CharField(max_length=100)

    def __str__(self):
        return self.city

class Room(models.Model):
    name = models.CharField(max_length=100)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    beds = models.IntegerField()
    status = models.CharField(choices =ROOM_STATUS,max_length = 15)
    price_per_night = models.IntegerField()
    available_from = models.DateField(auto_now_add=False)
    available_to = models.DateField(auto_now_add=False)
    picture1 = models.ImageField(upload_to='your_upload_path/', blank=True, null=True)
    picture2 = models.ImageField(upload_to='your_upload_path/', blank=True, null=True)
    picture3 = models.ImageField(upload_to='your_upload_path/', blank=True, null=True)

    @property
    def address(self):
        return self.location.address

    @property
    def city(self):
        return self.location.city


    def __str__(self):
        return self.name


class Reservation(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    guest = models.ForeignKey(User, on_delete= models.CASCADE)

    check_in = models.DateField(auto_now =False)
    check_out = models.DateField(auto_now =False)

    name = models.CharField(max_length=20, default="Name")
    surname = models.CharField(max_length=30)

    mail = models.EmailField()

    def __str__(self):
        return self.guest.username






