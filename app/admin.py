from django.contrib import admin
from models import Student, Room, Course, Hostel, User, Landlord

# Register your models here.
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['user', 'email', 'phone_no', 'department', 'paid']


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ['room_no', 'hostel_name']


@admin.register(Hostel)
class HostelAdmin(admin.ModelAdmin):
    list_display = ['name', 'gender', 'course']


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['code', 'room_type']

@admin.register(User)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['is_landlord']


@admin.register(Landlord)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['name']