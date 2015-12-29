from django.db import models

# Create your models here.

class Character(models.Model):
    name = models.CharField(max_length=200)
    speed = models.IntegerField(default=0)
    might = models.IntegerField(default=0)
    sanity = models.IntegerField(default=0)
    knowledge = models.IntegerField(default=0)

    def __str__(self):
        return self.name
