from django.db import models
from django.contrib.auth.models import User
import datetime

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg',upload_to='profile_pics')
    address = models.CharField(max_length=100)
    contact = models.CharField(max_length=15)
    alt_contact = models.CharField(max_length=15)
    Date_Of_Birth = models.DateField(default=datetime.date.today)
    def __str__(self):
        return f'{self.user.username} Profile'


class quiz(models.Model):
    quiz_name = models.CharField(max_length=50)
    def __str__(self) -> str:
        return self.quiz_name


class QuesModel(models.Model):
    Quiz = models.ForeignKey(quiz,on_delete=models.CASCADE,related_name="display")
    question = models.CharField(max_length=200)
    op1 = models.CharField(max_length=200)
    op2 = models.CharField(max_length=200)
    op3 = models.CharField(max_length=200)
    op4 = models.CharField(max_length=200)
    ans = models.CharField(max_length=200)

    def __str__(self):
        return self.question