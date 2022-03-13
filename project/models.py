from django.db import models

# Create your models here.
class Users(models.Model):
	uid = models.BigAutoField(primary_key = True)
	name = models.CharField(max_length = 50)
	email = models.CharField(max_length = 50)
	contact = models.CharField(max_length = 12)
	address = models.CharField(max_length = 60)
	username = models.CharField(max_length = 20, unique = True)
	password = models.CharField(max_length = 100)

class Admin(models.Model):
    aid = models.AutoField(primary_key = True)
    username = models.CharField(max_length = 50)
    password = models.CharField(max_length = 30)


class MeetingRooms(models.Model):
	room_id = models.BigAutoField(primary_key = True)
	meeting_room = models.CharField(max_length=100, unique = True)

class Reservation(models.Model):
	rid = models.AutoField(primary_key = True)
	username = models.ForeignKey(Users,to_field='username', on_delete=models.CASCADE)
	email = models.CharField(max_length = 50)
	contact = models.CharField(max_length = 12)
	date = models.DateField()
	timein = models.TimeField()
	timeout = models.TimeField()
	numpersons = models.CharField(max_length = 100)
	room = models.ForeignKey(MeetingRooms,to_field='room_id', on_delete=models.CASCADE)

class Payment(models.Model):
	 pid = models.AutoField(primary_key = True)

