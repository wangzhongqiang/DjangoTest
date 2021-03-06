import datetime

from django.db import models

# Create your models here.
from django.utils import timezone


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        now = timezone.now()
        return now >= self.pub_date >= now - datetime.timedelta(days=1)
    """ """
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = '最近发布'

class ThemeQuestion(Question):
    theme = models.CharField(max_length = 200)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text

'''----------------test------------------------'''


class Fruit(models.Model):
    name = models.CharField(max_length=100, primary_key=True)

class Apple(Fruit):
    custom = models.ManyToManyField(Fruit, related_name='testapple')

class Person(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):              # __unicode__ on Python 2
        return self.name

class Group(models.Model):
    name = models.CharField(max_length=128)
    members = models.ManyToManyField(Person, through='Membership')

    def __str__(self):              # __unicode__ on Python 2
        return self.name

class Membership(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    date_joined = models.DateField()
    invite_reason = models.CharField(max_length=64)
    def save(self, *args, **kwargs):
        print("this member ship save function")
        super(Membership, self).save(*args, **kwargs)

class CommonInfo1(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()

    class Meta:
        abstract = True

class Student1(CommonInfo1):
    home_group = models.CharField(max_length=5)


class CommonInfo2(models.Model):
    # ...
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    class Meta:
        abstract = True
        ordering = ['name']

class Student2(CommonInfo2):
    # ...
    class Meta(CommonInfo2.Meta):
        db_table = 'student_info'
class NewManager(models.Manager):
    # ...
    pass

class TestProxy(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    class Meta:
        abstract = True


class MyTestProxy(TestProxy):


    last_name = models.CharField(max_length=30)


    def do_something(self):
        # ...
        pass
"""
class OrderTestProxy(TestProxy):
    class Meta:
        ordering = ["last_name"]
        proxy = True
"""

class Blog(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField()

    def __str__(self):
        return self.name
    class Meta:
        ordering = ['name']

class Author(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()


    def __str__(self):
        return self.name

class EntityManager(models.Manager):
    def is_published(self):
        return True

class Entity(models.Model):
    objects = models.Manager()
    entities = EntityManager()
    blog = models.ForeignKey(Blog, related_name = 'entity_set' , null=True)
    #body_text = models.TextField()
    name = models.CharField(max_length=20, null=True)
    pub_date = models.DateField(null=True)
    headline = models.CharField(max_length=255)
    mod_date = models.DateField()
    datetime = models.DateTimeField(null=True)
    authors = models.ManyToManyField(Author)
    n_comments = models.IntegerField()
    n_pingbacks = models.IntegerField()
    rating = models.IntegerField()

    def __str__(self):
        return self.headline

class EntityDetail(models.Model):
    aentity = models.OneToOneField(Entity,on_delete=models.CASCADE)
    detail = models.TextField()

"""
class Event(models.Model):
   parent = models.ForeignKey(
       'self',
       on_delete=models.CASCADE,
       related_name='children',
   )
   date = models.DateField()
"""

class Topping(models.Model):
    name = models.CharField(max_length=30)

class Pizza(models.Model):
    name = models.CharField(max_length=50)
    toppings = models.ManyToManyField(Topping)

    def __str__(self):
        return "%s(%s)"%(
            self.name,", ".join(topping.name for topping in self.toppings.all()),
        )

class Restaurant(models.Model):
    pizzas = models.ManyToManyField(Pizza, related_name='restaurants')
    best_pizza = models.ForeignKey(Pizza, related_name='championed_by')


#----------------------test--------------------------
class CommonlyUsedModel(models.Model):
    f1 = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'app_largetable'

class ManagedModel(models.Model):
    f1 = models.CharField(max_length=10)
    f2 = models.CharField(max_length=10)

    class Meta:
        db_table = 'app_largetable'


class Chapter(models.Model):
    title = models.CharField(max_length=255, unique=True)

class Book(models.Model):
    title = models.CharField(max_length=256)
    chapters = models.ManyToManyField(Chapter)


class Boy2(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self):
        return self.name

class Mama2(models.Model):
    name = models.CharField(max_length=30)
    boys = models.ForeignKey(Boy2, on_delete=models.DO_NOTHING)