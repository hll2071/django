from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Question(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=200)
    modify_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField()
    create_date = models.DateTimeField()
    def __str__(self):
        return self.subject

class Answer(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    modify_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField()
    create_date = models.DateTimeField()

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    question = models.ForeignKey(Question, null=True, blank=True,
                                 on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, null=True, blank=True, on_delete=models.CASCADE)