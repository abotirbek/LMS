from django.shortcuts import render, redirect, get_object_or_404
from coins.models import CoinTransaction
from coins.coins_forms.coin_transaction_forms import CoinTransactionForm



def get_coin_transaction(request):
    coin_transaction = CoinTransaction.objects.all()
    return render(request, 'coins/coin_transaction/coin_transaction_list.html', {'coin_transaction': coin_transaction})


def create_coin_transaction(request):
    if request.method == 'POST':
        form = CoinTransactionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('coin_transaction_list')
    else:
        form = CoinTransactionForm()
    return render(request, 'coins/coin_transaction/create_coin_transaction.html', {'form': form})


def read_coin_transaction(request, pk):
    coin_transaction = get_object_or_404(CoinTransaction, pk=pk)
    return render(request, 'coins/coin_transaction/read_coin_transaction.html', {'coin_transaction': coin_transaction})


def update_coin_transaction(request, pk):
    coin_transaction = get_object_or_404(CoinTransaction, pk=pk)
    if request.method == 'POST':
        form = CoinTransactionForm(request.POST, instance=coin_transaction)
        if form.is_valid():
            form.save()
            return redirect('coin_transaction_list')
    else:
        form = CoinTransactionForm(instance=coin_transaction)
    return render(request, 'coins/coin_transaction/update_coin_transaction.html', {'form': form})


def delete_coin_transaction(request, pk):
    coin_transaction = get_object_or_404(CoinTransaction, pk=pk)
    if request.method == 'POST':
        coin_transaction.delete()
        return redirect('coin_transaction_list')
    return render(request, 'coins/coin_transaction/delete_coin_transaction.html', {'coin_transaction': coin_transaction})