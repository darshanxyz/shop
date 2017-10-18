from rest_framework.generics import ListAPIView, RetrieveAPIView
from items.models import Item
from .serializers import ItemSerializer

class ItemListAPIView(ListAPIView):
	queryset = Item.objects.all()
	serializer_class = ItemSerializer

class ItemRetrieveAPIView(RetrieveAPIView):
	queryset = Item.objects.all()
	serializer_class = ItemSerializer