from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

from django.dispatch import receiver

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    slug = models.CharField(max_length=100, blank=True , null=True)
    # ForeignKey many to one relationship, a single user can give multiple comments
    author = models.ForeignKey(User, on_delete = models.CASCADE) #user is the default table for to store our details
    created_date = models.DateField(max_length=50)
    body = models.CharField(max_length=500)

    def get_absolute_url(self):
        return reverse('article_detail',args=[self.id,self.slug])
    @receiver(pre_save,sender=Article)
    def slug_pre_save(sender,**kwargs):
         
