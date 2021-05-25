from django.shortcuts import render, redirect, HttpResponse
from .forms import fileuploadform
from .models import file_upload
from django.contrib import messages
# Create your views here.


def course3_content(request):

	if request.method == 'POST':
		c_form = fileuploadform(request.POST, request.FILES)
		if c_form.is_valid():
			name = c_form.cleaned_data['file_name']
			file = c_form.cleaned_data['files']
			file_upload(file_name=name, my_file=file).save()
			messages.success(request, ('File Added'))
			all_data = file_upload.objects.all()
			context = {'form': fileuploadform(), 'all_data':all_data}
			return render(request, 'course3/course3_content.html',context)
		#else:
			#return render(request,'course1/course1_content.html',{})	
		else:
			all_data = file_upload.objects.all()
			context = {'form': fileuploadform(), 'all_data':all_data}
			return render(request, 'course3/course3_content.html',context)
	else:
		all_data = file_upload.objects.all()
		context = {'form': fileuploadform(), 'all_data':all_data}
		return render(request, 'course3/course3_content.html',context)