from django.db import models
import os
#screen_shot from http://stackoverflow.com/questions/8189800/django-store-user-image-in-model
def get_image_path(instance,filename):
    return os.path.join('screen_shots',str(instance.id),filename)
# Create your models here.

class Complaint(models.Model):
    complain_id = models.AutoField(primary_key=True)
    text_box = models.CharField(max_length=4000)
    pub_date = models.DateTimeField('date created')
    screen_shot = models.ImageField(upload_to=get_image_path, max_length=2**20,blank=True, null=True) 
    original_document = models.FileField(upload_to='original_file', max_length=2**40,blank=True,null=True)

    def __str__(self):
        return self.complain_id
