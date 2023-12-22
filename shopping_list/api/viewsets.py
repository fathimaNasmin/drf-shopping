from rest_framework.viewsets import ModelViewSet
from .serializers import ShoppingItemSerializer
from shopping_list.models import ShoppingItem

class ShoppingItemViewSets(ModelViewSet):
    queryset = ShoppingItem.objects.all()
    serializer_class = ShoppingItemSerializer