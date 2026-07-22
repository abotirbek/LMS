from django.shortcuts import render, redirect, get_object_or_404
from .models import CoinTransaction, ShopItem, Purchase
from .forms import CoinTransactionForm, ShopItemForm, PurchaseForm

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

def get_shop_item(request):
    shop_item = ShopItem.objects.all()
    return render(request, 'coins/shop_item/shop_item_list.html', {'shop_item': shop_item})

def create_shop_item(request):
    if request.method == 'POST':
        form = ShopItemForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('shop_item_list')
    else:
        form = ShopItemForm()
    return render(request, 'coins/shop_item/create_shop_item.html', {'form': form})

def read_shop_item(request, pk):
    shop_item = get_object_or_404(ShopItem, pk=pk)
    return render(request, 'coins/shop_item/read_shop_item.html', {'shop_item': shop_item})

def update_shop_item(request, pk):
    shop_item = get_object_or_404(ShopItem, pk=pk)
    if request.method == 'POST':
        form = ShopItemForm(request.POST, request.FILES, instance=shop_item)
        if form.is_valid():
            form.save()
            return redirect('shop_item_list')
    else:
        form = ShopItemForm(instance=shop_item)
    return render(request, 'coins/shop_item/update_shop_item.html', {'form': form})

def delete_shop_item(request, pk):
    shop_item = get_object_or_404(ShopItem, pk=pk)
    if request.method == 'POST':
        shop_item.delete()
        return redirect('shop_item_list')
    return render(request, 'coins/shop_item/delete_shop_item.html', {'shop_item': shop_item})

def get_purchase(request):
    purchase = Purchase.objects.all()
    return render(request, 'coins/purchase/purchase_list.html', {'purchase': purchase})

def create_purchase(request):
    if request.method == 'POST':
        form = PurchaseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('purchase_list')
    else:
        form = PurchaseForm()
    return render(request, 'coins/purchase/create_purchase.html', {'form': form})

def read_purchase(request, pk):
    purchase = get_object_or_404(Purchase, pk=pk)
    return render(request, 'coins/purchase/read_purchase.html', {'purchase': purchase})

def update_purchase(request, pk):
    purchase = get_object_or_404(Purchase, pk=pk)
    if request.method == 'POST':
        form = PurchaseForm(request.POST, instance=purchase)
        if form.is_valid():
            form.save()
            return redirect('purchase_list')
    else:
        form = PurchaseForm(instance=purchase)
    return render(request, 'coins/purchase/update_purchase.html', {'form': form})

def delete_purchase(request, pk):
    purchase = get_object_or_404(Purchase, pk=pk)
    if request.method == 'POST':
        purchase.delete()
        return redirect('purchase_list')
    return render(request, 'coins/purchase/delete_purchase.html', {'purchase': purchase})