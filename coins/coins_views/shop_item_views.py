from django.shortcuts import render, redirect, get_object_or_404
from coins.models import ShopItem
from coins.coins_forms.shop_item_forms import ShopItemForm



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