from rest_framework import viewsets

# Create your views here.
from product_api.models import *
from product_api.serializers import *

class CategoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows category to be viewed or edited.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    # permission_classes = [permissions.IsAuthenticated]


class ItemViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows items to be viewed or edited.
    """
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    # permission_classes = [permissions.IsAuthenticated]