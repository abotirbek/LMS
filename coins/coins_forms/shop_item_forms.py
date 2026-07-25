from django import forms
from coins.models import ShopItem


class ShopItemForm(forms.ModelForm):
    class Meta:
        model = ShopItem
        fields = ['name', 'image', 'price', 'stock', 'is_active']