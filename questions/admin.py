from django.contrib import admin

# Register your models here.
from .models import Answer, Question, Tag, Profile

class UserAdmin(admin.ModelAdmin):
	fields = ['email', 'username', 'nickname', 'upload']

admin.site.register(Profile, UserAdmin)
admin.site.register(Question)
admin.site.register(Tag)
admin.site.register(Answer)