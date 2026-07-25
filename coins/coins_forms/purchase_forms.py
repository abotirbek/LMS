from django import forms
from coins.models import Purchase


class PurchaseForm(forms.ModelForm):
    class Meta:
        model = Purchase
        fields = ['student', 'item', 'status', 'transaction']