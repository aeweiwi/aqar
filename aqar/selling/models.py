from django.db import models
import json
# Create your models here.
class Owner(models.Model):
    fname=models.CharField(max_length=50)
    lname=models.CharField(max_length=50)
    email=models.EmailField()
    telnumbers=models.CharField(max_length=100) #This may contain multiple tel in a JSON format

    def set_telnumbers(self,x):
        self.telnumbers = json.dumps(x)

    def get_telnumbers(self):
        return json.loads(self.telnumbers) 
class House(models.Model):
    NUMBER_OF_ROOMS = [
        ("1","1"),
        ("2","2"),
        ("3","3"),
        ("4","4"),
        ("5","5"),
        ("6","6"),
        ("more","more")
    ]
    FLOOR_NUMBER = [
         ("1","1"),
        ("2","2"),
        ("3","3"),
        ("4","4"),
        ("5","5"),
        ("6","6"),
        ("7","7"),
        ("8","8"),
        ("9","9"),
        ("10","10"),
        ("more","more")
    ]
    address=models.CharField(max_length=200)#This will be a JSON address
    area=models.IntegerField()
    owner=models.ForeignKey(Owner, on_delete=models.CASCADE)
    price=models.IntegerField()
    imageurls=models.TextField() #This field contains the URLS of images inside house

    def set_address(self,x):
        self.address=json.dumps(x)

    def get_address(self):
        return json.load(self.address)

