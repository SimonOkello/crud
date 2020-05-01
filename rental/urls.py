from rest_framework import routers
from .views import FriendViewset, ItemViewset, BorrowedViewset
from rest_framework_extensions.routers import NestedRouterMixin

class NestedDefaultRouter(NestedRouterMixin, routers.DefaultRouter):
       pass
router = NestedDefaultRouter()
friends = router.register(r'friends', FriendViewset)
friends.register(
   r'borrowed',BorrowedViewset,
   basename='friend-borrow',
   parents_query_lookups=['friend'],
)

router.register(r'items', ItemViewset)
router.register(r'borrowed', BorrowedViewset)
