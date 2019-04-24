from django.contrib import admin

# Register your models here.
from django.contrib.auth.models import Permission

from polls.models import Poll, Choice, Question

class QuestionInLine(admin.StackedInline):
    model = Question
    extra = 1

class PollAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'start_date', 'end_date', 'del_flag']
    list_per_page = 10

    list_filter = ['start_date', 'end_date', 'del_flag', 'title']
    search_fields = ['title']

    # fields = ['']
    # exclude = ['']
    fieldsets = [
        ("Setter", {'fields':['title', 'del_flag']}),
        ("Active Duration", {'fields':['start_date', 'end_date'], 'classes':['collapse']})
    ]
    inlines = [QuestionInLine]

class ChoiceInLine(admin.TabularInline):
    model = Choice
    extra = 1

class ChoiceAdmin(admin.ModelAdmin):
    list_display = ['id', 'question', 'text', 'value']
    list_per_page = 15

    list_filter = ['question']

class QuestionAdmin(admin.ModelAdmin):
    list_display = ['id', 'poll', 'text']
    list_per_page = 15

    list_filter = ['poll']

    inlines = [ChoiceInLine]

admin.site.register(Poll, PollAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)
admin.site.register(Permission)
