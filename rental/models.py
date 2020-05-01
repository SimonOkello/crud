from django.db import models
from django.conf import settings

# Create your models here.
class OwnedModel(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL,
                              on_delete=models.CASCADE, null=True)

    class Meta:
        abstract = True
    


class Friend(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(default= '')

    def __str__(self):
        return self.name

    

class Item(OwnedModel):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name


class Borrowed(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    friend = models.ForeignKey(Friend, on_delete=models.CASCADE)
    when = models.DateTimeField(auto_now_add=True)
    returned_on = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Borrowed Items'

    def __str__(self):
        return f'{self.item} by {self.friend} on {self.when} to be returned on {self.returned_on}'
