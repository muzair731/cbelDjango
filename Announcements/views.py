from django.shortcuts import render, redirect
from .models import List
from .forms import ListForm
from django.contrib import messages
# Create your views here.
def home(request):
	if request.method == 'POST':
		form = ListForm(request.POST or None)
		if form.is_valid():
			form.save()
			all_items = List.objects.all
			messages.success(request, ('Item has been Added to List!'))
			return render(request, 'authenticate/home_todo.html', {'all_items': all_items})
	else:
		all_items = List.objects.all		
		return render(request, 'authenticate/home_todo.html', {'all_items': all_items})

def delete(request, list_id):
	item = List.objects.get(pk=list_id)
	item.delete()
	messages.success(request, ('Item has been Deleted'))
	return redirect('home_todo')

def cross_off(request, list_id):
	item = List.objects.get(pk=list_id)
	item.completed = True
	item.save()
	return redirect('home_todo')

def uncross(request, list_id):
	item = List.objects.get(pk=list_id)
	item.completed = False
	item.save()
	return redirect('home_todo')	
def edit(request, list_id):
	if request.method == 'POST':
		item = List.objects.get(pk=list_id)
		form = ListForm(request.POST or None, instance = item)

		if form.is_valid():
			form.save()
			messages.success(request, ('Item has been Edited!'))
			return redirect('home_todo')
	else:
		item = List.objects.get(pk=list_id)		
		return render(request, 'authenticate/edit.html', {'item': item})
