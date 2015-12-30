from django.db import models

# Create your models here.

class Character(models.Model):
    name = models.CharField(max_length=200)

    image = models.CharField(max_length=200)
    color = models.CharField(max_length=200)

    speed_options = models.CharField(max_length=200)
    might_options = models.CharField(max_length=200)
    sanity_options = models.CharField(max_length=200)
    knowledge_options = models.CharField(max_length=200)

    speed_index = models.IntegerField(default=0)
    might_index = models.IntegerField(default=0)
    sanity_index = models.IntegerField(default=0)
    knowledge_index = models.IntegerField(default=0)

    def __str__(self):
        return self.name
