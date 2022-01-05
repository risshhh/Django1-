from django.shortcuts import render, get_object_or_404,redirect
from .forms import PersonForm
from .forms import StudentForm, PerForm, SignupForm, LoginForm
from .models import Person


from django.contrib.auth import (
	authenticate,
	login,
	logout,
	)

# Create your views here.
def home(request):
	if request.user.is_authenticated:
		form = PersonForm(request.POST or None)
		if form.is_valid():
			name = form.cleaned_data.get('name')
			std = form.cleaned_data.get('std')
			college = form.cleaned_data.get('college')
			branch = form.cleaned_data.get('branch')

			new = Person()
			new.name = name
			new.std = std
			new.college = college
			new.branch = branch

			new.save()
			form = PersonForm()
		context = {
			'form':form
		}
		return render(request,'home.html',context)
	else:
		return redirect('/login/')

def about(request):
	#add data from normal django form
	form = StudentForm(request.POST or None)
	if form.is_valid():
		name = form.cleaned_data.get('name')
		regno = form.cleaned_data.get('regno')
		subject = form.cleaned_data.get('subject')

		new = Student()
		new.name = name
		new.regno = regno
		new.subject = subject

		new.save()
		form = StudentForm()
	context = {
		'form1':form
	}
	return render(request,'about.html',context)

def contactus(request):
	#add data from the ModelForm
	form = PerForm(request.POST or None)
	if form.is_valid():
		new = form.save(commit = False)
		new.save()
		form = PerForm()
	context = {
		'form':form
	}
	return render(request,'contactus.html',context)

def thankyou(request):
	#to add data from the HTML form
	if request.method == 'POST':
		name = request.POST['name']
		std = request.POST['std']
		college = request.POST['college']
		branch = request.POST['branch']
		instance = Person()
		instance.name = name
		instance.std = std
		instance.college = college
		instance.branch = branch
		instance.save()

	return render(request,'ty.html',{})


def all_person(request):
	#retreive all objects
	result = Person.objects.all().order_by('-id')
	context = {
		'list':result
	}
	return render(request,'all.html',context)



def single_view(request,id=None):
	#get single single object data
	#instance = Person.objects.get(id=id)
	instance = get_object_or_404(Person,id=id)
	context = {
		'instance':instance
	}
	return render(request,'single.html',context)



def signup_view(request):
	form = SignupForm(request.POST or None)
	if form.is_valid():
		new = form.save(commit=False)
		password = form.cleaned_data.get('password')
		confirm_password = form.cleaned_data.get('confirm_password')
		if password==confirm_password:
			new.set_password(password)
			new.save()
	context = {
		'form':form
	}
	return render(request,'signup.html',context)


def login_view(request):
	form = LoginForm(request.POST or None)
	if form.is_valid():
		username = form.cleaned_data.get('username')
		password = form.cleaned_data.get('password')
		user = authenticate(username=username,password=password)
		try:
			login(request,user)
			return redirect('/')
		except:
			return redirect('/login/')
	context = {
		'form':form
	}
	return render(request,'login.html',context)



def logout_view(request):
	logout(request)
	return redirect('/login/')