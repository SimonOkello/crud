import django_filters
from rest_framework import viewsets
from .models import Friend, Item, Borrowed
from .serializers import FriendSerializer, ItemSerializer, BorrowedSerializer
from .permissions import IsOwner
from rest_framework.permissions import IsAuthenticated
from django.db import models
import pendulum
from rest_framework.decorators import action
from rest_framework.response import Response
from django.core.mail import send_mail
from rest_framework_extensions.mixins import NestedViewSetMixin
from rest_flex_fields import FlexFieldsModelViewSet

# Create your views here.

class FriendViewset(NestedViewSetMixin,viewsets.ModelViewSet):
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


class BorrowedFilterSet(django_filters.FilterSet):
    missing = django_filters.BooleanFilter(field_name="returned_on", lookup_expr="isnull")
    overdue = django_filters.BooleanFilter(method="get_overdue", field_name="returned_on")

    class Meta:
        model = Borrowed
        fields = ["item", "friend", "missing", "overdue"]

    def get_overdue(self, queryset, field_name, value):
        if value:
            return queryset.overdue()
        return queryset


class BorrowedViewset(NestedViewSetMixin,FlexFieldsModelViewSet):
    queryset = Borrowed.objects.all().select_related('friend', 'item')
    permit_list_expands = ['item', 'friend']
    serializer_class = BorrowedSerializer
    permission_classes = [IsAuthenticated]
    filterset_class = BorrowedFilterSet

    @action(detail=True, url_path = 'remind', methods = ['post'])
    def remind_single(self, request, *args, **kwargs):
        obj = self.get_object()
        send_mail(
            subject = f"Please return my item:{obj.item.name}",
            message=f'You forgot to return my item: "{obj.item.name}" that you borrowed on {obj.when}. Please return it.',
            from_email="simonokello.dev@gmail.com",  # your email here
            recipient_list=[obj.friend.email],
            fail_silently=False
        )
        return Response("Email Sent!")
