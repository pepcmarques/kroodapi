from rest_framework import serializers

from .models import Item


class ItemSerializer(serializers.ModelSerializer):
    """
    {
     "category": "food",
     "subcategory": "vegetables",
     "name": "potato",
     "amount": 25
    }
    """
    class Meta:
        model = Item
        fields = ('category', 'subcategory', 'name', 'amount')
