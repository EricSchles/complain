from django.shortcuts import render
from logger.models import Complaint

# Create your views here.
def index(request):
    return render(request, "logger/index.html")

def log(request):
    data = Complaint()
    #add sending data to the database
    return render(request, "logger/success.html")
