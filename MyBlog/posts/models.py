from django.db import models

# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=100)
    icerik=models.TextField().null
    created_date=models.DateTimeField(auto_now_add=True)
    updated_date= models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return "%s"%(self.title) #admin panelinde title yi gösterir