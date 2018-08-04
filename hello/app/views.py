from django.shortcuts import render,redirect
from app.forms import RegistrationForm,EditProfileForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm,PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
# Create your views here.
def home(request):

	return render(request,'app/home.html')
def register(request):
	if request.method=='POST':
		form=RegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/app')
	else:
		form=RegistrationForm()

		args={'form':form}
		return render(request,'app/reg_form.html',args)
def view_profile(request):
	args={'user':request.user}
	return render(request,'app/profile.html',args)

def edit_profile(request):
	if request.method=='POST':
		form=EditProfileForm(request.POST,instance=request.user)

		if form.is_valid():
			form.save()
			return redirect('/app/profile')
	else:
		form=EditProfileForm(instance=request.user)
		args={'form': form}
		return render(request,'app/edit_profile.html',args)

def change_password(request):
	if request.method=='POST':
		form=PasswordChangeForm(data=request.POST,user=request.user)

		if form.is_valid():
			form.save()
			update_session_auth_hash(request,form.user)
			return redirect('/app/profile')
		else:
			return redirect('/account/change-password')
	else:
		form=PasswordChangeForm(user=request.user)
		args={'form': form}
		return render(request,'app/change_password.html',args)
