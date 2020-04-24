from rest_framework import viewsets
from .models import Friend, Item, Borrowed
from .serializers import FriendSerializer, ItemSerializer, BorrowedSerializer
from .permissions import IsOwner
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class FriendViewset(viewsets.ModelViewSet):
    queryset = Friend.objects.all()
    serializer_class = FriendSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return super().get_queryset().annotate(
            ann_overdue=models.Case(
                models.When(borrowed__when__lte=pendulum.now().subtract(months=2), then=True),
                default=models.Value(False),
                output_field = models.BooleanField()
            )
        )

class ItemViewset(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [IsOwner, IsAuthenticated]

class BorrowedViewset(viewsets.ModelViewSet):
    queryset = Borrowed.objects.all()
    serializer_class = BorrowedSerializer
    permission_classes = [IsAuthenticated]
