from django.contrib import admin

# Register your models here.
from .models import Question,Choice

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


admin.site.register(Question, QuestionAdmin)

