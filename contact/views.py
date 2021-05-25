from django.shortcuts import render
from .forms import contactformemail
from django.core.mail import send_mail
# Create your views here.

def contactsendmail(request):
	if request.method == 'GET':
		form = contactformemail()
	else:
		form = contactformemail(request.POST)
		if form.is_valid():
			frommail=form.cleaned_data['email']
			subject=form.cleaned_data['subject']
			message=form.cleaned_data['message']
			send_mail(subject,message,frommail,['chuzair1236@gmail.com',frommail])
	return render(request, 'contact/contact.html', {'form':form})

