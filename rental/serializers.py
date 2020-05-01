from rest_framework import serializers
from . models import Friend, Borrowed, Item, OwnedModel
import pendulum
from rest_flex_fields import FlexFieldsModelSerializer

class FriendSerializer(FlexFieldsModelSerializer):
   
    has_overdue = serializers.SerializerMethodField()

   
    class Meta:
        model = Friend
        fields = ('id', 'name', 'email', 'has_overdue')

    def get_has_overdue(self, obj):
        if hasattr(obj, 'ann_overdue'):
            return obj.ann_overdue
        return obj.borrowed_set.filter(
            returned_on__isnull=True, when=pendulum.now().subtract(months=2)
        ).exists()

class ItemSerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    class Meta:
        model = Item
        fields = ('id', 'name', 'owner')
    
class BorrowedSerializer(FlexFieldsModelSerializer):
    expandable_fields = {
        "item": (ItemSerializer, {'source': 'item'}),
        "friend": (FriendSerializer, {'source': 'friend'})
    }
    class Meta:
        model = Borrowed
        fields = ('id', 'item', 'friend', 'when', 'returned_on')
