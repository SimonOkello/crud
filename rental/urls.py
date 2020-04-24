from rest_framework import routers
from .views import FriendViewset, ItemViewset, BorrowedViewset

router = routers.DefaultRouter()
router.register(r'friends', FriendViewset)
router.register(r'items', ItemViewset)
router.register(r'borrowed', BorrowedViewset)
