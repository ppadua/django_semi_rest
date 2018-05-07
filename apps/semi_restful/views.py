from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime
from apps.semi_restful.models import *

def index(request):
	return render(request, "semi_restful/index.html", { "users" : User.objects.all() })

def new(request):
	return render(request, "semi_restful/add.html")

def create(request):
	if request.method == "POST" :
		user = User()
		user.first_name = request.POST['first_name']
		user.last_name = request.POST['last_name']
		user.email = request.POST['email']
		user.save()

	return redirect("/users")

def show(request, number):
	if request.method == "POST":
		user = User.objects.filter(id=request.POST["user_id"]).first()
		user.first_name = request.POST['first_name']
		user.last_name = request.POST['last_name']
		user.email = request.POST['email']
		user.save()

	return render(request, "semi_restful/show_user.html",  { "user" : User.objects.filter(id=number).first() })

def edit(request, number):
	return render(request, "semi_restful/update.html",  { "user" :User.objects.filter(id=number).first() })

def destroy(request, number):
	user = User.objects.filter(id=number)
	user.delete()

	return redirect("/users")


# Create your views here.
