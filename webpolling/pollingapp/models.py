from django.db import models
from django import forms
from django.core import validators
def checkID(value):
    if len(str(value)) != 12:
        raise forms.ValidationError("Enter a valid voter ID")
# Create your models here.
class UserInfoID(models.Model):
    id_number = models.PositiveIntegerField(unique=True, validators=[checkID])
    first_name = models.CharField(max_length = 20)
    last_name = models.CharField(max_length = 20)
    gender = models.CharField(max_length = 5)

    def __str__(self):
        return self.first_name + self.last_name

class PartyVotes(models.Model):
    person = models.OneToOneField(UserInfoID, on_delete=models.CASCADE)
    party = models.CharField(max_length=15)
    def __str__(self):
        return self.person.first_name + self.person.last_name
