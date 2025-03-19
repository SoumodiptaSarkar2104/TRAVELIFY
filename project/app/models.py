from django.db import models

# Create your models here.
class userdata(models.Model):
  Name=models.CharField(max_length=100)
  DOB=models.DateField()
  Email=models.EmailField()
  Contact=models.IntegerField()
  Place=models.CharField(max_length=100)
  Gender=models.CharField(max_length=100)
  Country=models.CharField(max_length=100)
  Password=models.CharField(max_length=50)
  class Meta:
    db_table="userdata"
class picfile(models.Model):
    pname=models.CharField(max_length=100)
    purl=models.ImageField()
    class Meta:
        db_table="picfile"

# Create your models here.
class Image(models.Model):
    photo=models.ImageField(upload_to="myimage")
    date=models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table="Image"

# models.py
from django.db import models

class Review(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    rating = models.PositiveIntegerField(default=5)  # Rating out of 5 stars
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review by {self.name} from {self.location}"
    

from django.db import models

class Comment(models.Model):
    description = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.description[:50]

class Reply(models.Model):
    comment = models.ForeignKey(Comment, related_name='replies', on_delete=models.CASCADE)
    description = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.description[:50]

from django.db import models

class Message(models.Model):
    user_name = models.CharField(max_length=100)
    text = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user_name}: {self.text[:50]}"

from django.db import models

class RentalSubmission(models.Model):
    duration = models.IntegerField()
    license = models.CharField(max_length=10)  # Yes or No
    budget = models.DecimalField(max_digits=10, decimal_places=2)
    persons = models.IntegerField()
    driver_needed = models.CharField(max_length=10)  # Yes or No

    def __str__(self):
        return f"Rental for {self.duration} days - Budget: ₹{self.budget}"
