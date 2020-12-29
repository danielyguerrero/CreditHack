from django.shortcuts import render, redirect, reverse
from .models import Account

# Create your views here.
def index(request):
	context = {
	'accts':Account.objects.all()
	}
	return render(request,'credit/index.html', context)


def add(request):

	account = Account.objects.create_acct(request.POST)
	
	return redirect(reverse("dashboard"))




def create(request):
	return	render(request, 'credit/create.html')