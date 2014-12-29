from django.db import models
import os
#screen_shot from http://stackoverflow.com/questions/8189800/django-store-user-image-in-model
#better example: http://stackoverflow.com/questions/5871730/need-a-minimal-django-file-upload-example -- file upload
def get_image_path(filename):
    return os.path.join('media',filename)
# Create your models here.

class Complaint(models.Model):
    complain_id = models.AutoField(primary_key=True)
    text_box = models.CharField(max_length=4000,blank=True,null=True)
    pub_date = models.DateTimeField('date created',blank=True,null=True)
    screen_shot = models.ImageField(upload_to=get_image_path, max_length=2**20,blank=True, null=True) 
    original_document = models.FileField(upload_to=get_image_path, max_length=2**40,blank=True,null=True)

    def __str__(self):
        return str(self.complain_id)
