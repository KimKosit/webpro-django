"""
    `models.py`
    Contains database model of `polls` application
"""

from django.db import models

class Poll(models.Model):
    title = models.CharField(max_length=100)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    del_flag = models.BooleanField(default=False)

    def __str__(self):
        return '{}'.format(self.title)

class Question(models.Model):
    TYPES = (
        ('01', 'Single answer'),
        ('02', 'Multiple answers'),
    )
    text = models.TextField()
    type = models.CharField(max_length=2, choices=TYPES, default='01')
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)

    def __str__(self):
        return '{} - {}'.format(self.poll.title, self.text)

class Choice(models.Model):
    text = models.CharField(max_length=100)
    value = models.IntegerField(default=0)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return '{} - {}'.format(self.question, self.text)

class Answer(models.Model):
    choice = models.OneToOneField(Choice, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

class Comment(models.Model):
    title = models.CharField(max_length=100)
    body = models.CharField(max_length=500)
    email = models.EmailField()
    tel = models.CharField(max_length=10)
