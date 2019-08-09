from django.db import models

# Create your models here.
class Bar(models.Model):
    title = models.CharField(max_length=255, default='null')
    image = models.ImageField(upload_to='images/')
    description = models.CharField(max_length=500)
    posit = models.CharField(max_length=500, default='null')
    url = models.CharField(max_length=500, default='null')
    centerx = models.CharField(max_length=255, default = '37.3595704')
    centery = models.CharField(max_length=255, default = '127.105399')

    def __str__(self):
        return self.title

class Blog(models.Model):
    title = models.CharField(max_length=200)           
    pub_date = models.DateTimeField('date published')  
    body = models.TextField()                          

    def __str__(self):      
        return self.title

    def summary(self):
        return self.body[:100] 