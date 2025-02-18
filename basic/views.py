from django.shortcuts import redirect, render, get_object_or_404
from basic.forms import *
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required, user_passes_test
from django.views.decorators.csrf import csrf_protect
from django_ratelimit.decorators import ratelimit

def is_admin(user):
    return user.is_superuser

@csrf_protect
@user_passes_test(is_admin) 
@login_required
@ratelimit(key='ip', rate='5/m', method='ALL')
def add_course(request):
    add_quiz = quizform()
    if request.method == 'POST':
        add_quiz = quizform(request.POST)
        if add_quiz.is_valid():
            add_quiz.save()
        else:
            messages.error(request, 'Form is invalid')
        return redirect('/')
    return render(request, 'addQuiz.html', {'quiz_form': add_quiz})

def home(request):
    Quiz = quiz.objects.all()
    if request.method == 'POST':
        quiz_id = request.POST.get("quiz")
        if quiz_id:
            redirect_url = reverse("display", args=[quiz_id])
            return redirect(redirect_url)
    return render(request, 'home.html', {'obj': Quiz})

@ratelimit(key='ip', rate='5/m', method='ALL')
@csrf_protect
def register(request):
    if request.method == 'POST':
        data1 = RegisterForm(request.POST)
        if data1.is_valid():
            data1.save()
            return redirect('/login')
        messages.error(request, "Please enter the details correctly")
    data1 = RegisterForm()
    return render(request, 'register.html', context={'form': data1})

@ratelimit(key='ip', rate='5/m', method='ALL')
@csrf_protect
def dj_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('/')
            messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request, 'login.html', context={"login_form": form})

@login_required
def loggout(request):
    logout(request)
    return redirect('login')

@ratelimit(key='ip', rate='5/m', method='ALL')
@login_required
def profile(request):
    return render(request, 'profile.html', {'user': request.user})

@ratelimit(key='ip', rate='5/m', method='ALL')
@login_required
@csrf_protect
def profup(request):
    if request.method == 'POST':
        u_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid():
            u_form.save()
            messages.success(request, "Profile Updated Successfully")
            return redirect("prof")
    else:
        u_form = ProfileUpdateForm(instance=request.user.profile)
    return render(request, 'Profile_update.html', {'u_form': u_form})

@ratelimit(key='ip', rate='5/m', method='ALL')
@user_passes_test(is_admin)
@login_required
@csrf_protect
def addQuestion(request):
    add_ques = addQues()
    quiz_name = quiz.objects.all()
    if request.method == 'POST':
        add_ques = addQues(request.POST)
        if add_ques.is_valid():
            question = add_ques.save()
            messages.success(request, "Question added successfully")
        else:
            messages.error(request, 'Form is invalid')
        return redirect('/')
    return render(request, 'addQues.html', {'add_ques': add_ques, 'quiz_name': quiz_name})

@ratelimit(key='ip', rate='5/m', method='ALL')
@login_required
@csrf_protect
def ques(request, course_id):
    quiz_name = get_object_or_404(quiz, id=course_id)
    if request.method == "POST":
        questions = quiz_name.display.all()
        score, wrong, correct, total = 0, 0, 0, 0

        for question in questions:
            user_answer = request.POST.get(question.question)
            if user_answer and user_answer == question.ans:
                score += 10
                correct += 1
            else:
                wrong += 1
            total += 1

        percent = int(score / (total * 10) * 100) if total else 0
        context = {
            'score': score,
            'correct': correct,
            'total': total,
            'wrong': wrong,
            'percent': percent
        }
        return render(request, 'result.html', context)

    return render(request, 'ques.html', {'display': quiz_name})
