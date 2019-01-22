from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('hot/', views.best_questions, name='hot'),
	path('tag/<slug:tag>/', views.by_tag, name='by_tag'),
	path('question/<int:question_id>', views.question, name='question'),
	path('login/', views.login_view, name='login'),
	path('signup/', views.registration, name='signup'),
	path('ask/', views.ask, name='ask'),
	path('search/', views.search, name='search'),
	path('logout/', views.logout_view, name='logout'),
	path('settings/', views.settings, name='settings'),
]