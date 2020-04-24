from django.contrib import admin
from .models import Friend, Item, Borrowed

# Register your models here.
admin.site.register(Friend)
admin.site.register(Item)
admin.site.register(Borrowed)
