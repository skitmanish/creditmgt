from django.shortcuts import render
from django.shortcuts import render,redirect,get_object_or_404
from proview.models import Proview
def profile(request,profile_id):
    profile=get_object_or_404(Proview,pk=profile_id)

    ids=()
    for user in Proview.objects.all():
        if user.id != profile_id:
            ids=(ids+(user.id,))

    print(ids)
    others=Proview.objects.filter(id__in=ids)


    return render(request,'profile.html',{'profile':profile,'others':others})
