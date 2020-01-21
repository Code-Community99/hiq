from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import feeds_list
from signup.models import signup_user
from .forms import feedform
from comments.models import comment_list

def Feeds(request):

    try:
        request.session["email"]

    except:
        return redirect("/login/")

    else:
        if request.method == "POST":
            pass

        else:
            updates = feeds_list.objects.order_by("-post_time")
            online_users = []

            filler = signup_user.objects.filter(logstatus=True)

            for user in filler:
                online_users.append(user.First_Name)

            return render(request , "./Feeds/feeds.html" , context = {"updates" : updates,"online_users":online_users})




def addFeeds(request):
    useremail = ""

    try:
        useremail = request.session["email"]

    except:
        return redirect("/login/")

    else:

        if request.method =="POST":
            feed = request.POST["feed"]
            uid = signup_user.objects.get(Email = useremail).uid
            feeds_list.objects.create(uid_id = uid , feed = feed)

            return redirect("/Feeds/")

        else:

            form = feedform()
            return render(request , "./Feeds/addfeed.html" , context = {"form":form})
