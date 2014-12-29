from django.shortcuts import render
from logger.models import Complaint
from django.http import HttpResponse
from datetime import datetime


# Create your views here.
def index(request):
    #to do: make sure picture has picture extensions only.
    
    # print request.GET.get("screen_shot")
    # complaint = Complaint(
    #     text_box=request.GET.get('text_box'),
    #     screen_shot=request.GET.get("screen_shot"),
    #     original_document=request.GET.get("original_document"),
    #     pub_date = datetime.now()
    # )
    # if complaint.text_box != None:
    #     complaint.save()

    
    return render(request, "logger/index.html")

