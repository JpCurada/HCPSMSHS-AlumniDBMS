from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import AddRecordForm
from .models import Record
from .filters import RecordFilter

from django.http import HttpResponse, HttpResponseRedirect
import csv

# Create your views here.
def home(request):
	record_filter = RecordFilter(request.GET, queryset=Record.objects.all())
	all_records_count = Record.objects.all().count()
	records_count = record_filter.qs.count()

	context = {'form': record_filter.form, 
	    	   'records':record_filter.qs, 
			   'records_count': records_count, 
			   'all_records_count':all_records_count}
	
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']

		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			return redirect('home')
		else:
			messages.success(request, "There was an error loggin in. Please try again.")
	
	return render(request, 'home.html', context)

def records_csv(request):
	
	response = HttpResponse(content_type='text/csv')
	response['Content-Disposition'] = 'attachment; filename=alumni_records.csv'
	# Create a csv writer
	writer = csv.writer(response)
	# Designate the model
	records = Record.objects.all()

	# Create header names
	writer.writerow(['Sex', 'Strand', 'Batch', 'University', 'Course'])

	for record in records:
		writer.writerow([record.sex, record.strand, record.graduation_year, record.college_university, record.college_course])
	
	return response
	


def logout_user(request):
    logout(request)
    return redirect('home')

def meet_the_team(request):
    return render(request, 'about_us.html', {})

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
		form = AddRecordForm(request.POST or None, instance=current_record)
		if form.is_valid():
			form.save()
			messages.success(request, "Record Has Been Updated!")
			return redirect('home')
		return render(request, 'update_record.html', {'form':form})
	else:
		messages.success(request, "You Must Be Logged In...")
		return redirect('home')
	


