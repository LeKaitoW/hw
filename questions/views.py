#from django.shortcuts import render
from django.shortcuts import HttpResponse, get_object_or_404, render, redirect
from django.core.paginator import Paginator
from django.utils import timezone
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from .models import Question, Answer, Tag
from .forms import QuestionForm, AnswerForm, RegisterForm

# Create your views here.

def paginate(objects_list, request):
    paginator = Paginator(objects_list, 30)
    page = request.GET.get('page')
    objects_page = paginator.get_page(page)
    return objects_page, paginator

def base_template(request):
    context = dict()
    if request.user.is_authenticated:
        context['base_template'] = 'questions/authenticated.html'
        context['user'] = request.user
    else:
        context['base_template'] = 'questions/base.html'
    return context

def index(request):
    latest_questions = Question.objects.order_by('-date')
    latest, _ = paginate(latest_questions, request)
    context = {'latest_questions': latest}
    context.update(base_template(request))
    return render(request, 'questions/index.html', context)

def best_questions(request):
    hot_questions = Question.objects.order_by('-rate')
    hot, _ = paginate(hot_questions, request)
    context = {'hot_questions': hot}
    context.update(base_template(request))
    return render(request, 'questions/hot.html', context)

def by_tag(request, tag):
    tags = get_object_or_404(Tag, word=tag)
    questions = Question.objects.by_tag(tag)
    context = {'by_tag': questions}
    context.update(base_template(request))
    return render(request, 'questions/tag.html', context)

def question(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            inst = form.save(commit=False)
            inst.date = timezone.now()
            inst.question = question
            inst.correct = False
            inst.author = request.user
            inst.save()
            return redirect('question', question_id=question_id)
    else:
        form = AnswerForm()
        all_answers = Answer.objects.filter(question_id=question.pk)
        answers, _ = paginate(all_answers, request)
        tags = Tag.objects.filter()
        context = {'form':form, 'question':question, 'answers':answers }
        context.update(base_template(request))
    return render(request, 'questions/question.html', context)

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return HttpResponse("Invalid")
    else:
        form = AuthenticationForm()
    context = {'form':form}
    context.update(base_template(request))
    return render(request, 'questions/login.html', context)

def registration(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            inst = form.save(commit=False)
            inst.set_password(inst.password)
            inst.is_active = True
            inst.save()
            return redirect('login')
    else:
        form = RegisterForm()
    context = {'form':form}
    context.update(base_template(request))
    return render(request, 'questions/signup.html', context)

def ask(request):
    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            inst = form.save(commit=False)
            inst.date = timezone.now()
            inst.author = request.user
            inst.save()
            return redirect('question', question_id=inst.pk)
    else:
        form = QuestionForm()
        context = {'form':form}
        context.update(base_template(request))
        return render(request, "questions/ask.html", context)


def search(request):
    search_str = request.GET.get("search_str")
    themed_posts = Question.objects.filter(title__icontains=search_str)
    context = {'themed_posts' : themed_posts, 'search_str' : search_str}
    context.update(base_template(request))
    return render(request, "questions/search.html", context)

def logout_view(request):
    logout(request)
    return redirect('index')