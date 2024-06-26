from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddRecordForm
from .models import Record

def home(request):
    
    records = Record.objects.all()

    # Check to see if logging in
    if request.method == 'POST': ## filling the login form and posting it
        username = request.POST['username']
        password = request.POST['password']

        # Authenticate
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You Have Been Logged In!")

            ## path('', views.home, name='home'), and again run this "home" function [[[def home]]]
            ## at last [[  return render(request, 'home.html', {} ) ]] may be ----sn=
            return redirect('home')
        else:
            messages.success(request, "There Was An Error Logging In, Please Try Again...")

            ## home ==== home.html  ---- may be ---- self note --sn=
            return redirect('home')
    else:
        return render(request, 'home.html', {'records': records} )


def logout_user(request):
	logout(request)
	messages.success(request, "You Have Been Logged Out...")
	return redirect('home')


def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # Authenticate and login
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "You Have Successfully Registered! Welcome!")
            return redirect('home')
    else:
        form = SignUpForm()
        return render(request, 'register.html', {'form':form})

    return render(request, 'register.html', {'form':form})



def customer_record(request, pk):
	if request.user.is_authenticated:
		# Look Up Records
		customer_record = Record.objects.get(id=pk)
		return render(request, 'record.html', {'customer_record':customer_record})
	else:
		messages.success(request, "You Must Be Logged In To View That Page...")
		return redirect('home')



def delete_record(request, pk):
	if request.user.is_authenticated:
		delete_it = Record.objects.get(id=pk)
		delete_it.delete()
		messages.success(request, "Record Deleted Successfully...")
		return redirect('home')
	else:
		messages.success(request, "You Must Be Logged In To Do That...")
		return redirect('home')




def add_record(request):
    form = AddRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                add_record = form.save()
                messages.success(request, "Record Added...")
                return redirect('home')
        return render(request, 'add_record.html', {'form':form})
    else:
        messages.success(request, "You Must Be Logged In...")
        return redirect('home')



def update_record(request, pk):
	if request.user.is_authenticated:
		current_record = Record.objects.get(id=pk)
        
        ## first step ------  pass instance of current_record --- propogate form ((fill form with already available data))
        ## second step ------ request.POST (user want to post the form)---- None(user is editing the form and want to post)
		form = AddRecordForm(request.POST or None, instance=current_record)
            
		if form.is_valid():
			form.save()
			messages.success(request, "Record Has Been Updated!")
			return redirect('home')

        ## when before POSTing of form, update_record.html is rendered and 
        ## then, again form.is_valid function of if statement is run if form POST is happened (update_record view run twice) self note sn=
		return render(request, 'update_record.html', {'form':form})
      
	else:
            
		messages.success(request, "You Must Be Logged In...")
		return redirect('home')
