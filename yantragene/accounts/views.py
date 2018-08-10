from django.conf import settings
from django.shortcuts import render, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import (

	authenticate,
	login,
	logout

	)

from .models import Profile
from events.models import Participant


def register_view(request):
	if request.method=="POST":
		first_name=request.POST['fname']
		last_name=request.POST['lname']
		username=request.POST['uname']
		password=request.POST['pwd']
		cpassword=request.POST['cpwd']
		email=request.POST['email']
		mobile=request.POST['mobile']

		u = User.objects.filter(username=username)
		if len(u):
			return render(request,'accounts/register.html', {'msg':"Username already been taken"})
		e = User.objects.filter(email=email)
		if len(e):
			return render(request,'accounts/register.html', {'msg':"Email Already registered"})
		if len(mobile)!=10:
			return render(request,'accounts/register.html', {'msg':"Please enter Correct Mobile Number"})
		m = Profile.objects.filter(mobile=mobile)
		if len(e):
			return render(request,'accounts/register.html', {'msg':"Mobile number already existed"})
		if password!=cpassword:
			return render(request,'accounts/register.html', {'msg':"Password And Confirm Password Did not Match"})

		user, create = User.objects.get_or_create(
			
			first_name=first_name,
			last_name=last_name,
			username=username,
			email=email,

			)
		
		user.set_password(password)
		user.save()
		pro = Profile(mobile=mobile, user=user)
		pro.save()

		return HttpResponseRedirect(reverse('accounts:login'))
	else:
		return render(request,'accounts/register.html', {'msg':""})

def login_view(request):
	if request.method=="POST":
		username=request.POST['uname']
		password=request.POST['pwd']
		try:
			user = authenticate(username=username,password=password)
			if user is not None:
				login(request, user)
				return HttpResponseRedirect(reverse('home:home'))

			else:
				return render(request, 'accounts/login.html', {'msg':"Wrong Username Or Password"})
		except:
			return render(request, 'accounts/login.html', {'msg':"Sorry, Error In Login"})
	else:
		return render(request, 'accounts/login.html', {'msg':""})

def logout_view(request):
	logout(request)
	return HttpResponseRedirect(reverse('home:home'))


def profile_view(request, id=None):
	participant = Participant.objects.filter(profile=id)
	context = {
		'participant':participant,
		'length':len(participant)
	}

	return render(request, 'accounts/profile.html', context)

def delete_event(request, id=None, proid=None):
	
	try:
		p = Participant.objects.get(id=id)
		p.delete()
	except:
		pass
	finally:
		return HttpResponseRedirect(reverse('accounts:profile', kwargs={'id': proid }))