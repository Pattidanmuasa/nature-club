from django.forms import forms
from django.http import request
from django.shortcuts import render,redirect
from django.views import generic
from .models import *
from blog.models import *
from .forms import *
from django.contrib import messages

from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm

from django.db.models import Q
from django.views.generic import  ListView,View,CreateView#,DetailView,TemplateView,

def Home(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request,user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("/")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	leaders = LeaderShip.objects.all()
	sliders = Slider.objects.all()
	services = Activities.objects.all()
	return render(request, 'nature_club/Home.html', {'leaders':leaders,'sliders':sliders,'services':services})


def About(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request,user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("/")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	items = Team.objects.all()
	return render(request, 'nature_club/About.html',{'items':items})




def Contact(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request,user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("/")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			form.save() # saves in database
			messages.success(request, f"Your message has been sent.Thanks for visiting our site!")
	else:
		form = ContactForm()
	return render(request,'nature_club/Contact.html',{'form': form})


def gallery(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request,user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("/")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	images = Gallery.objects.all()
	return render(request, 'nature_club/Gallery.html', {'images':images})


        
class SearchResultsView(ListView):
    model = Post
    template_name = 'blog/search_results.html'
	
    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Post.objects.filter(Q(title__icontains=query) | Q(content__icontains=query)|Q(status__icontains=query))
        return object_list
	
# def SearchResultsView(request):
#     query = request.GET.get('q','')
#     #The empty string handles an empty "request"
#     if query:
#             queryset = (Q(title__icontains=query) | Q(content__icontains=query)|Q(status__icontains=query))
#             #I assume "text" is a field in your model
#             #i.e., text = model.TextField()
#             #Use | if searching multiple fields, i.e., 
#             #queryset = (Q(text__icontains=query))|(Q(other__icontains=query))
#             results = Post.objects.filter(queryset).distinct()
#     else:
# 		request.method == "POST":
# 		form = AuthenticationForm(request, data=request.POST)
# 		if form.is_valid():
# 			username = form.cleaned_data.get('username')
# 			password = form.cleaned_data.get('password')
# 			user = authenticate(username=username, password=password)
# 			if user is not None:
# 				login(request,user)
# 				messages.info(request, f"You are now logged in as {username}.")
# 				return redirect("/")
# 			else:
# 				messages.error(request,"Invalid username or password.")
# 		else:
# 			messages.error(request,"Invalid username or password.")
# 	form = AuthenticationForm()
# 	return render(request, 'blog/search_results.html', {'results':results, 'query':query})
	   
    

#     #You can also set context = {'results':results, 'query':query} after 
#     #the else: (same indentation as return statement), and 
#     #use render(request, 'home.html', context) if you prefer.



###########The subcoms #####################
def tree(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request,user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("/")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	# images = Gallery.objects.all()
	return render(request, 'nature_club/tree.html')

def bird(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request,user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("/")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	# images = Gallery.objects.all()
	return render(request, 'nature_club/bird.html')

def debate(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request,user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("/")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	# images = Gallery.objects.all()
	return render(request, 'nature_club/debate.html')


###########The executive #####################
def presid(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request,user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("/")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	# images = Gallery.objects.all()
	return render(request, 'nature_club/pred.html')

def editor(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request,user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("/")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	# images = Gallery.objects.all()
	return render(request, 'nature_club/editor.html')

def sec(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request,user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("/")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	# images = Gallery.objects.all()
	return render(request, 'nature_club/sec.html')