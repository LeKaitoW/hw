from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

class Tag(models.Model):
	word = models.CharField(max_length=20, unique=True)

	def __str__(self):
		return self.word


class Profile(AbstractUser):
	nickname = models.CharField(max_length=20, unique=True)
	upload = models.ImageField(upload_to='uploads/%Y/%m/%d/', default='uploads/default/default.png')


class QuestionManager(models.Manager):
	def get_queryset(self):
		return super().get_queryset().annotate(answer_count=models.Count('answers'))

	def get_by_id(self, id):
		return get_object_or_404(Question, id)

	def get_most_hot(self):
		return self.get_queryset().order_by('-answer_count')

class TagManager(models.Manager):
	def get_queryset(self):
		return super().get_queryset()

	def get_most_popular(self, count):
		return self.get_queryset().annotate(num_question=models.Count('questions')).order_by('-num_question')[:count]


class Tag(models.Model):
	word = models.CharField(max_length=20, unique=True)
	objects = TagManager()

	def __str__(self):
		return self.word


class Profile(AbstractUser):
	nickname = models.CharField(max_length=20, unique=True)
	upload = models.ImageField(upload_to='uploads/%Y/%m/%d/', default='uploads/default/default.png')


	@staticmethod
	def get_tag_by_title(tag):
		return get_object_or_404(Tag, title=tag)

	def get_by_tag(self, tag):
		return self.get_queryset().filter(tags=QuestionManager.get_tag_by_title(tag))


class Question(models.Model):
	title = models.CharField(max_length=80)
	text = models.TextField(max_length=500)
	author = models.ForeignKey(Profile, on_delete=models.CASCADE)
	date = models.DateTimeField('date published')
	tags = models.ManyToManyField(Tag, related_name='questions')
	rate = models.IntegerField(default=0)
	objects = QuestionManager()

	def publish(self):
		self.date = timezone.now()
		self.save()

	def __str__(self):
		return self.title

	# class Meta:
	# 	ordering = ['-create_date']


class Answer(models.Model):
	question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
	text = models.TextField(max_length=200)
	author = models.ForeignKey(Profile, on_delete=models.CASCADE)
	date = models.DateTimeField('date published')
	correct = models.BooleanField()
	rate = models.IntegerField(default=0)

	def __str__(self):
		return self.text

	# class Meta:
	# 	ordering = ['-create_date']
