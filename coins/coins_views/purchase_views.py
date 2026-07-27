from django.db import transaction
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from coins.models import Purchase
from coins.coins_forms.purchase_forms import PurchaseForm
from coins.models import ShopItem
from coins.models import CoinTransaction


def get_purchase(request):
    purchase = Purchase.objects.all()
    return render(request, 'coins/purchase/purchase_list.html', {'purchase': purchase})

@transaction.atomic
def create_purchase(request, pk):
    student = request.user.student_profile
    item = ShopItem.objects.select_for_update().get(pk=pk)
    # item = get_object_or_404(ShopItem, pk=pk)

    if item.stock <= 0:
        return HttpResponse("Mahsulot qolmagan!")
    elif student.coin_balance < item.price:
        return HttpResponse("Mablag' yetarli emas!")
    else:
        item.stock -= 1
        item.save()



    coin_transaction = CoinTransaction.objects.create(
        student=student,
        amount=-item.price,
        reason=CoinTransaction.Reason.PURCHASE,
        created_by=request.user,
        comment=f"Purchased {item.name}",
    )


    Purchase.objects.create(
        student=student,
        item=item,
        status=Purchase.Status.PENDING,
        transaction=coin_transaction,
    )
    return redirect('shop_item_list')


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