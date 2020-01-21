from django.shortcuts import render,redirect
from .models import comment_list
from django.http import HttpResponse
from .forms import commentform
from signup.models import signup_user
from Feeds.models import feeds_list



def commentview(request , feedid):
    try:
        request.session["email"]
    except:
        return redirect("/login")

    else:
        form = commentform()
        fid = feedid
        feedcontent = feeds_list.objects.get(Fid = fid)
        
        comments = comment_list.objects.filter(fid_id = feedid).order_by("comment_post_time")
        return render(request , "./comments/comments.html/" , context = {"comments":comments , "form":form,"fid":fid , "fidcontent":feedcontent})




def addcomment(request):
    try:
        request.session["email"]
    except:
        return redirect("/login")

    else:
        form = commentform()

        fid = request.POST['fid']

        cuid = signup_user.objects.get(Email = request.session["email"]).uid

        comments = comment_list.objects.filter(fid = request.POST['fid'])

        comment_list.objects.create(uid_id = cuid,fid_id = request.POST['fid'] , comments = request.POST["comments"])

        return redirect("/comments/{}/#test".format(fid))
