from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('hot/', views.best_questions, name='hot'),
	path('tag/<slug:tag>/', views.by_tag, name='by_tag'),
	path('question/<int:question_id>/', views.question, name='question'),
	path('login/', views.login, name='login'),
	path('signup/', views.registration, name='signup'),
	path('ask/', views.ask, name='ask'),
]