from django import forms
from coins.models import CoinTransaction

class CoinTransactionForm(forms.ModelForm):
    class Meta:
        model = CoinTransaction
        fields = ['student', 'amount', 'reason', 'comment']