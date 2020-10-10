from django.contrib import admin
from  .models import Item, Comment, Category

# Register your models here.
admin.site.register(Item)
admin.site.register(Comment)
admin.site.register(Category)


