from django.db import models
from django.utils import timezone

# Create your models here.
class Tag(models.Model):
	word = models.CharField(max_length=20)

	def __str__(self):
		return self.word


class Question(models.Model):
	title = models.CharField(max_length=80)
	text = models.CharField(max_length=200)
	author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
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
	text = models.CharField(max_length=200)
	author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
	date = models.DateTimeField('date published')
	correct = models.BooleanField()
	rate = models.IntegerField(default=0)

	def __str__(self):
		return self.text


class Profile(models.Model):
	user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
	