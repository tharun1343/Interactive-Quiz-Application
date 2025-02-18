from operator import mod
from django.shortcuts import redirect, render
from basic.forms import *
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.

def add_course(request):
	add_quiz = quizform()
	if request.method == 'POST':
		add_quiz = quizform(request.POST)
		if add_quiz.is_valid():
			add_quiz.save()
		else:
			print('form is invalid')
		return redirect('/')
	return render(request,'addQuiz.html',{'quiz_form':add_quiz})

def home(request):
	Quiz = quiz.objects.all()
	if request.method == 'POST':
		quiz_id = request.POST.get("quiz")
		if quiz_id is not None:
			arguments = quiz_id
			redirect_url = reverse("display",args=arguments)
			return redirect(redirect_url)
	return render(request,'home.html',{'obj':Quiz})


# function for registration.
def register(request):
    if request.method == 'POST':
        data1 = RegisterForm(request.POST)
        if data1.is_valid():
            data1.save()
            return redirect('/login')
        messages.error(request,"Please enter the details correctly")
    data1 = RegisterForm()
    return render(request,'register.html',context={'form' : data1})

# function for user login.
def dj_login(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request,user)
				return redirect('/')
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request,'login.html', context={"login_form":form})

# function for user logout.
def loggout(request):
	logout(request)
	return redirect('login')

# function for profile page.
def profile(request):
	context = {
		'user': request.user
	}
	return render(request,'profile.html',context)

def profup(request):
	if request.method == 'POST':
		u_form = ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
		if u_form.is_valid():
			u_form.save()
			messages.success(request,"Profile Updated Successfully")	  
			return redirect("prof")
	u_form= ProfileUpdateForm(instance=request.user.profile)
	context ={'u_form': u_form}
	return render(request,'Profile_update.html',context)

def addQuestion(request):
	add_ques = addQues()
	quiz_name = quiz.objects.all()
	if request.method == 'POST':
		add_ques = addQues(request.POST)
		if add_ques.is_valid():
			question = add_ques.save()
			question.save()
		else:
			print('form is invalid')
		return redirect('/')
	return render(request,'addQues.html',{'add_ques':add_ques,'quiz_name':quiz_name})

def ques(request,course_id):
	quiz_name = quiz.objects.get(id=course_id)
	if request.method=="POST":
		print(request.POST)
		questions= quiz.objects.get(id=course_id)
		score = 0
		wrong = 0
		correct = 0
		total = 0
		for x in questions.display.all():
			if x.ans == request.POST.get(x.question):
				score +=10
				correct +=1
				total +=1
			else:
				wrong+=1
				total+=1
		percent = int(score/(total*10)*100)
		context ={
			'score':score,
			'correct':correct,
			'total':total,
			'wrong':wrong,
			'percent':percent
		}
		return render(request,'result.html',context)
	return render(request,'ques.html',{'display':quiz_name})

