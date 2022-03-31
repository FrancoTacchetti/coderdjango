from django.db import models

class FamilyMember(models.Model):
    name = models.CharField(max_length=40)
    dob = models.DateField()
    member_id = models.IntegerField()