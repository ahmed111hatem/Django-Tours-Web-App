from django.db import models

# Create your models here.
class tour(models.Model):
# We Need --> (Origin Country, destination, Num_Of_Nights, Price)
  origin_country = models.CharField(max_length=64)
  destination = models.CharField(max_length=64)
  Num_Of_Nights = models.IntegerField()
  price = models.IntegerField()
  # This is a string represttation of the tours

  def __str__(self):
    return(f"ID:[{self.id}],  From: {self.origin_country},  To: {self.destination},  Number Of The Nights To The Customer: {self.Num_Of_Nights},  Price Of The Destination: ${self.price}")

