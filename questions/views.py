#from django.shortcuts import render
from django.shortcuts import HttpResponse, get_object_or_404, render

from .models import Question

# Create your views here.
def index(request):
	latest_questions = Question.objects.order_by('-date')[:10]
	context = {'latest_questions':latest_questions,}
	return render(request, 'questions/index.html', context)

def best_questions(request):
	hot_questions = Question.objects.order_by('-rate')[:10]
	context = {'hot_questions':hot_questions,}
	return render(request, 'questions/hot.html', context)

def by_tag(request, tag):
	questions = Question.objects.all()[:10]
	context = {'by_tag':questions,}
	return render(request, 'questions/tag.html', context)

def question(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	return render(request, 'questions/question.html', {'question': question})

def login(request):
	return HttpResponse("Login!!")

def registration(request):
	return HttpResponse("Reg!!")

def ask(request):
	return HttpResponse("Ask!!")