from django.shortcuts import render, redirect, get_object_or_404
from coins.models import Purchase
from coins.coins_forms.purchase_forms import PurchaseForm



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