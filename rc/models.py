from django.db import models

# Create your models here.
class user_register_model(models.Model):
    model_username=models.CharField(max_length=30)
    model_firstname=models.CharField(max_length=30)
    model_lastname=models.CharField(max_length=30)
    model_email=models.EmailField(primary_key=True)
    model_phone=models.IntegerField(max_length=10)
    model_password=models.CharField(max_length=30)

    def __str__(self):
        return 'Username:{},Name:{} {},Email:{},phone:{}'.format(self.model_username,self.model_firstname,self.model_lastname,self.model_email,self.model_phone)
   