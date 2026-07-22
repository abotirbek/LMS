from django import forms
from .models import CoinTransaction, Purchase, ShopItem

class CoinTransactionForm(forms.ModelForm):
    class Meta:
        model = CoinTransaction
        fields = ['student', 'amount', 'reason', 'comment']

class ShopItemForm(forms.ModelForm):
    class Meta:
        model = ShopItem
        fields = ['name', 'image', 'price', 'stock', 'is_active']

class PurchaseForm(forms.ModelForm):
    class Meta:
        model = Purchase
        fields = ['student', 'item', 'status', 'transaction']