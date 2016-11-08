from django.db import  models

class Fruit1(models.Model):
    name = models.Field
class Fruit(models.Model):
    name = models.ForeignKey(
        Fruit1,
        on_delete=models.CASCADE
    )