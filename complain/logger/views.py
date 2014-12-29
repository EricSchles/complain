from django.shortcuts import render
from logger.models import Complaint
from django.http import HttpResponse
from datetime import datetime
from logger.forms import ComplaintForm



# Create your views here.
def index(request):
    #to do: make sure picture has picture extensions only.
    
    form = ComplaintForm(request.POST, request.FILES)

    complaint = Complaint(
        text_box=request.GET.get('text_box'),
        screen_shot=request.FILES["screen_shot"],
        original_document=request.FILES["original_document"],
        pub_date = datetime.now()
    )
    if complaint.text_box != None:
        complaint.save()
    
        

    return render(request, "logger/index.html")

