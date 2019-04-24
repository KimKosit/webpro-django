"""
    forms.py
    Contains classes to create forms
"""

from django import forms
from django.core import validators
from django.core.exceptions import ValidationError
from polls.models import Poll


class PollForm(forms.Form):
    title = forms.CharField(label='Poll title', max_length=100, required=True)
    question_amount = forms.IntegerField(label='Question amount', min_value=1, max_value=10, required=True)
    start_date = forms.DateField(required=False)
    end_date = forms.DateField(required=False)

    def clean_title(self):
        data = self.cleaned_data['title']

        if len(data) < 6:
            raise ValidationError('Title is too short!')

        return data

    def clean(self):
        cleaned_data = super().clean()
        start = cleaned_data.get('start_date')
        end = cleaned_data.get('end_date')

        if (start and not end):
            self.add_error('end_date', 'Please input end date.')

        elif (not start and end):
            self.add_error('start_date', 'Please input start date.')

class PollModelForm(forms.ModelForm):
    title = forms.CharField(label='Poll title', max_length=100, required=True)
    question_amount = forms.IntegerField(label='Question amount', min_value=1, max_value=10, required=True)
    class Meta:
        model = Poll
        exclude = ['del_flag']

    def clean_title(self):
        data = self.cleaned_data['title']

        if len(data) < 6:
            raise ValidationError('Title is too short!')

        return data

    def clean(self):
        cleaned_data = super().clean()
        start = cleaned_data.get('start_date')
        end = cleaned_data.get('end_date')

        if (start and not end):
            self.add_error('end_date', 'Please input end date.')

        elif (not start and end):
           self.add_error('start_date', 'Please input start date.')

def isNum(data):
    try:
        int(data)
        return True
    except ValueError:
        return False

class CommentForm(forms.Form):
    title = forms.CharField(max_length=99, required=True)
    body = forms.CharField(max_length=499, required=True)
    email = forms.EmailField(required=False)
    tel = forms.CharField(max_length=10, required=False)



    def clean(self):
        cleaned_data = super().clean()

        if  ((not cleaned_data['email']) and (not cleaned_data['tel'])):
            raise ValidationError('Please input E-Mail, Phone No.')

        if ((not cleaned_data['email']) and (len(cleaned_data['tel']) != 10)) or ((not cleaned_data['email']) and isNum(cleaned_data['tel']) == False):
            raise ValidationError('Please input valid Phone No. || Phone No. should be 10 numbers.')