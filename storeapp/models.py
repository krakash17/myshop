from django.db import models
# from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _ # If you need optional
from phone_field import PhoneField


def uploadcategoryimage_path(instance, filname):
    return '/'.join(['categoryimage', str(instance.category_name), filname])

def uploadprofileimage_path(instance, filname):
    return '/'.join(['profileimage', str(instance.image), filname])    

# If you want to customize the Default user model you can Inherit the Abstract user model
class User(AbstractUser):
    username = models.CharField(max_length=40, unique=True)
    email = models.EmailField(_('email address'), unique=True)
    phone = PhoneField(blank=True, help_text='Contact phone number')
    image = models.FileField(blank=True, null=True,upload_to=uploadprofileimage_path )
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'first_name','password','image' 'last_name','phone']

    def __str__(self):
        return "{}".format(self.email)

# 

class Categories(models.Model):
    category_name = models.CharField(max_length=20, unique=True)
    picture = models.FileField(blank=True, null=True,upload_to=uploadcategoryimage_path )

class SubCategories(models.Model):
    category_id = models.IntegerField()
    subcategory_name = models.CharField(max_length=20, unique=True)

class Item(models.Model):
     subcategory_id = models.IntegerField()
     item_name = models.CharField(max_length=30,unique=True)
     item_description = models.CharField(max_length=75,unique=True)
     item_price = models.IntegerField()
     item_amount = models.IntegerField(default=0)
     item_flag = models.BooleanField()
     item_quantity = models.CharField(max_length=20,unique=True)

      