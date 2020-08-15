from django.shortcuts import render,redirect,get_object_or_404
from proview.models import Proview
from record.models import Trecord

from datetime import datetime
# Create your views here.
def home(request):
    return render(request,'details/details.html')

def viewprofiles(request):
    profiles=Proview.objects
    return render(request,'details/viewprofiles.html',{'profiles':profiles})

def contact(request):
    return render(request,'details/contact.html')

def record(request):

    records=Trecord.objects.order_by('-pk')
    return render(request,'details/record.html',{'records':records})

def transfer(request):

    fname=request.POST['fname']
    tname=request.POST['toname']
    profile1=get_object_or_404(Proview,name=fname)
    profile2=get_object_or_404(Proview,name=tname)
    amt=request.POST['amount']
    print(fname)
    print(tname)
    if amt.isnumeric() and int(amt)>0:

        if int(request.POST['amount'])<=profile1.credits:
            profile1.credits=profile1.credits-int(request.POST['amount'])
            profile2.credits=profile2.credits+int(request.POST['amount'])
            record=Trecord()

            record=Trecord(fname=request.POST['fname'],tname=request.POST['toname'],amount=request.POST['amount'],event_date=datetime.now())
            record.save()
            profile1.save()
            profile2.save()
            return redirect('/record')
        else:
            ids=()
            for user in Proview.objects.all():
                if user.id != profile1.id:
                    ids=(ids+(user.id,))
            message='Please Enter a credit amount less than or equal to Available Credits'
            #print(ids)
            others=Proview.objects.filter(id__in=ids)
            return render(request,'profile.html',{'profile':profile1,'others':others,'message':message})
    else:
        ids=()
        for user in Proview.objects.all():
            if user.id != profile1.id:
                ids=(ids+(user.id,))

        #print(ids)
        others=Proview.objects.filter(id__in=ids)
        message='Please enter a valid integer credit amount'
        return render(request,'profile.html',{'profile':profile1,'others':others,'message':message})
