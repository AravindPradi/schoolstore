from django.db import models


class Team(models.Model):
    name = models.CharField(max_length=100)
    designation = models.TextField()
    image = models.ImageField(upload_to='teamImage')


    def __str__(self):
        return self.name