from django.db import models

# Create your models here.
class Itinerary(models.Model):
    user_id=models.CharField(max_length=100)
    destination=models.CharField(max_length=100)
    start_date=models.DateField()
    end_date=models.DateField()
    budget=models.IntegerField()
    no_of_people=models.IntegerField()
    plan = models.JSONField()

def __str__(self):
    return f"{self.destination } - {self.user_id}"