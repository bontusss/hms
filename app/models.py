from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    is_landlord = models.BooleanField(default=False)

class Student(models.Model):
    user = models.OneToOneField(User, default=None, null=True, on_delete=models.CASCADE)
    email = models.EmailField(unique=True)
    phone_no = models.CharField(max_length=11)
    department = models.CharField(null=True, max_length=100)
    room  = models.OneToOneField('Room', on_delete=models.CASCADE)
    dob = models.DateField(
        max_length=10,
        help_text="format : YYYY-MM-DD",
        null=True)
    gender_choices = [('M', 'Male'), ('F', 'Female')]

    gender = models.CharField(
        choices=gender_choices,
        max_length=1,
        default=None,
        null=True)
    paid = models.BooleanField(default=False)
    room_allotted = models.BooleanField(default=False)


    def __str__(self) -> str:
        return self.user.username


class Room(models.Model):
    room_no = models.CharField(max_length=4, null=True)
    hostel_name = models.CharField(max_length=100, null=True)
    room_choice = [('S', 'Single Occupancy'), ('D', 'Double Occupancy'), ('P', 'Reserved for Research Scholars'),('B', 'Both Single and Double Occupancy')]
    room_type = models.CharField(choices=room_choice, max_length=1, default=None)
    vacant = models.BooleanField(default=False)


    def __str__(self):
        return self.room_no

class Hostel(models.Model):
    name = models.CharField(max_length=5)
    gender_choices = [('M', 'Male'), ('F', 'Female')]
    gender = models.CharField(
        choices=gender_choices,
        max_length=1,
        default=None,
        null=True)
    course = models.ManyToManyField('Course', default=None, blank=True)
    landlord = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name


class Course(models.Model):
    # if a student has enrollment number iit2017001 then the course code is iit2017
    code = models.CharField(max_length=100, default=None)
    room_choice = [('S', 'Single Occupancy'), ('D', 'Double Occupancy'), ('P', 'Reserved for Research Scholars'), ('B', 'Both Single and Double Occupancy')]
    room_type = models.CharField(choices=room_choice, max_length=1, default='D')

    def __str__(self):
        return self.code


class Landlord(models.Model):
    name = models.CharField(max_length=100, null=True)
    phone_no = models.PhoneNumberField(null=True)
    email = models.EmailField(null=True, max_length=254)