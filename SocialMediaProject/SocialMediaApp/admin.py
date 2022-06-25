from django.contrib import admin
from .models import Article
#here createing the AdminArticle for to display our model in table format
class AdminArticle(admin.ModelAdmin):
    list_display = ['title','slug','author','created_date','body']
    prepopulated_fields = {'slug':('title',)}

# Register your models here.
admin.site.register(Article,AdminArticle)
