from django.contrib import admin

# Register your models here.
from .models import Answer, Question, Tag

admin.site.register(Question)
admin.site.register(Tag)
admin.site.register(Answer)