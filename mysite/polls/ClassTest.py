from django.db import  models
from django.db.models import Prefetch
from django.db.models import QuerySet
from django.db.models.functions import Coalesce


class Fruit1(models.Model):
    name = models.Field
class Fruit(models.Model):
    name = models.ForeignKey(
        Fruit1,
        on_delete=models.CASCADE
    )


Fruit.objects.bulk_create()

