import datetime

from django.shortcuts import render


# Create your views here.
def index(request):
    now = datetime.datetime.now()
    return render(request, "hannah/index.html", {
        "birthday": now.month == 4 and now.day == 26
    })
