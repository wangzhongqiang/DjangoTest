from django.contrib import admin

# Register your models here.
from .models import *

#admin.site.register(Question)

"""
admin.site.register(Choice)

class QuestionAdmin(admin.ModelAdmin):
    #fields = ['pub_date', 'question']
    fieldsets = [
        (None,                  {'fields':['question_text']}),
        ('Date information',    {'fields':['pub_date']}),
    ]

admin.site.register(Question, QuestionAdmin)
"""

#class ChoiceInLine(admin.StackedInline):
class ChoiceInLine(admin.TabularInline):
    model = Choice
    extra = 2

class QuestionAdmin(admin.ModelAdmin):
    """
    fieldsets = [
        (None,                  {'fields':['question_text']}),
        ('Date information',   {'fields':['pub_date'],'classes':['collapse']}),
    ]
    inlines = [ChoiceInLine]
    """
    search_fields = ['question_text','pub_date']
    list_filter = ['pub_date']
    list_display = ('pub_date','was_published_recently','question_text',)

class BlogAdmin(admin.ModelAdmin):

    search_fields = ['name','tagline']

class AUthorAdmin(admin.ModelAdmin):

    search_fields = ['name','email']

class EntityAdmin(admin.ModelAdmin):

    search_fields = ['headline','pub_date']
    list_display = ('blog', 'headline', 'rating',"pub_date")

class BoyAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields=['name']
class MamaAdmin(admin.ModelAdmin):
    list_display = ('name','boys')
class ToppingAdmin(admin.ModelAdmin):
    search_fields = ['name']
class PizzaAdmin(admin.ModelAdmin):
    search_fields = ['name']
    pass
class RestaurantAdmin(admin.ModelAdmin):
    pass
admin.site.register(Choice)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Author, AUthorAdmin)

admin.site.register(Blog, BlogAdmin)
admin.site.register(Entity, EntityAdmin)

admin.site.register(Topping,ToppingAdmin)
admin.site.register(Pizza,PizzaAdmin)
admin.site.register(Restaurant,RestaurantAdmin)

admin.site.register(CommonlyUsedModel)
admin.site.register(ManagedModel)
admin.site.register(Chapter)
admin.site.register(Book)
admin.site.register(Person)
admin.site.register(Boy2,BoyAdmin)
admin.site.register(Mama2,MamaAdmin)

class Search(models.Lookup):
    lookup_name = 'search'

    def as_mysql(self, compiler, connection):
        lhs, lhs_params = self.process_lhs(compiler, connection)
        rhs, rhs_params = self.process_rhs(compiler, connection)
        params = lhs_params + rhs_params
        s = 'MATCH (%s) AGAINST (%s IN BOOLEAN MODE)' % (lhs, rhs), params
        print('0---------')
        print(s)
        return s


models.CharField.register_lookup(Search)
models.TextField.register_lookup(Search)