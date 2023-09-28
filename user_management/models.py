from django.db import models

class User(models.Model):
    name = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='user_photos/', null=True, blank=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    mobile_number = models.CharField(max_length=15)
    date_of_birth = models.DateField()

    def __str__(self):
        return self.name

