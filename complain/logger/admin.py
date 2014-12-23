from django.contrib import admin
from logger.models import Complaint

class ComplaintAdmin(admin.ModelAdmin):
    list_display = ("complain_id","text_box","pub_date")
# Register your models here.
admin.site.register(Complaint,ComplaintAdmin)
