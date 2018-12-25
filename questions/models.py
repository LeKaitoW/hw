from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

class Tag(models.Model):
	word = models.CharField(max_length=20, unique=True)

	def __str__(self):
		return self.word


class Profile(AbstractUser):
	nickname = models.CharField(max_length=20, unique=True)


class Question(models.Model):
	title = models.CharField(max_length=80)
	text = models.TextField(max_length=500)
	author = models.ForeignKey(Profile, on_delete=models.CASCADE)
	date = models.DateTimeField('date published')
	tags = models.ManyToManyField(Tag)
	rate = models.IntegerField(default=0)

	def publish(self):
		self.date = timezone.now()
		self.save()

	def __str__(self):
		return self.title


class Answer(models.Model):
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	text = models.TextField(max_length=200)
	author = models.ForeignKey(Profile, on_delete=models.CASCADE)
	date = models.DateTimeField('date published')
	correct = models.BooleanField()
	rate = models.IntegerField(default=0)

	def __str__(self):
		return self.text
