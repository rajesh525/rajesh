from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import friends
from .forms import nameform
# Create your views here.

def raj(request):
    r=friends.objects.all()
    return HttpResponse("thank you for using django ")
def nm(request):
    if request.method=='POST':
	    form=nameform(request.POST)
	    if form.is_valid():
		    nm=form.cleaned_data['yourname']
		    subject=form.cleaned_data['subject']
            p=friends(name=nm,friend=subject)
            p.save()
            return HttpResponseRedirect('form/')

def nmform(request):
    frm=nameform
    return render(request,'raj/form.html',{'form':frm})
def img(request,img):
    return render(request,'raj/vi.html',{'nm':img})
