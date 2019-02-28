from django.shortcuts import render

from .forms import SignInForm
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect


def index(request):
	if request.user.is_authenticated:
	    return render(request, 'projects/index.html')
	else:
		return redirect('/projects/sign_in/')

def sign_in(request):
	if request.method == 'POST':
		form = SignInForm(request.POST)

		if form.is_valid():
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)

				return redirect('/projects/')

			else:
				form = SignInForm()
				return render(request, 'projects/sign_in.html', {'form': form})
	else:
		form = SignInForm()
    
	return render(request, 'projects/sign_in.html', {'form': form})

def sign_out(request):
	logout(request)

	return redirect('/projects/sign_in/')