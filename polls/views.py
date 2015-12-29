from django.shortcuts import render
from django.http import HttpResponse
from .models import Artical,raj,Reporter,profit
from django.shortcuts import get_object_or_404
from django.db.models import Q,Count

# Create your views here.

def index(request):
    return  render(request,'polls/events.html')

def raj(request):
    return HttpResponse("rajesh is good")
def year_arch(request,year):
    a_list=Artical.objects.filter(pub_date=year)
    context={'year':year,'artl_list':a_list}
    return render(request,'polls/sub.html',context)
def  stud(request,rol):
    std= get_object_or_404(raj, rollno=rol)
    st={'slist':std}
    return render(request,'polls/stdl.html',st)
def intd(request):
    st=Reporter(full_name=request.POST['fname'])
    st.save()
    return HttpResponse("thanyou for registring")
def std(request):
    return render(request,'polls/sub.html')
def art(request):
    r=Artical(pub_date=request.POST['pdate'],headline=request.POST['hd'],content=request.POST['con'])
    r.save()
    return  HttpResponse("thank you for registring artical....")
def ar(request):
    return render(request,'polls/art.html')
def gt(request):
    rj=Artical.objects.all().order_by('headline') [:5]
    return render(request,'polls/rj.html',{'artl_list':rj})
def pro(request):
    rj=profit.objects.filter(Q(name='saranya') & Q(rno='14a95a0514'))
    tr=profit.objects.aggregate(Count('name'))
    return render(request,'polls/rock.html',{'pro':rj,'t':tr})
    
