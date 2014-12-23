from django.shortcuts import render
from logger.models import Complaint
from django.http import HttpResponse
from datetime import datetime
# Create your views here.
def index(request):
    #to do: make sure picture has picture extensions only.
    complaint = Complaint(
        text_box=request.GET.get('text_box'),
        screen_shot=request.GET.get("screen_shot"),
        original_document=request.GET.get("original_document"),
        pub_date = datetime.now()
    )
    complaint.save()
    return render(request, "logger/index.html")

def log(request):
    data = Complaint()
    #add sending data to the database
    return render(request, "logger/success.html")
