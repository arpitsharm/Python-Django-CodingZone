from django.db import models

# Create your models here.
class ContactUs(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    phone_num = models.CharField(max_length=20)
    message = models.TextField()

    def __str__(self):
        return self.name
    
class Apps(models.Model):
    name = models.CharField(max_length=100)
    file = models.CharField(max_length=100)
    image = models.ImageField(upload_to='apps')

    def __str__(self):
        return self.name