from rest_framework import serializers
from . models import Friend, Borrowed, Item, OwnedModel

class FriendSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = Friend
        fields = ('id', 'name')

class ItemSerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    class Meta:
        model = Item
        fields = ('id', 'name', 'owner')
    
class BorrowedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Borrowed
        fields = ('id', 'item', 'friend', 'when', 'returned_on')
