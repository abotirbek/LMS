from django.urls import path
from coins.coins_views import coin_transaction_views, purchase_views, shop_item_views

urlpatterns = [
    path('transactions/', coin_transaction_views.get_coin_transaction, name='coin_transaction_list'),
    path('transactions/create/', coin_transaction_views.create_coin_transaction, name='create_coin_transaction'),
    path('transactions/<int:pk>/', coin_transaction_views.read_coin_transaction, name='read_coin_transaction'),
    path('transactions/<int:pk>/update/', coin_transaction_views.update_coin_transaction, name='update_coin_transaction'),
    path('transactions/<int:pk>/delete/', coin_transaction_views.delete_coin_transaction, name='delete_coin_transaction'),

    path('shop-items/', shop_item_views.get_shop_item, name='shop_item_list'),
    path('shop-items/create/', shop_item_views.create_shop_item, name='create_shop_item'),
    path('shop-items/<int:pk>/', shop_item_views.read_shop_item, name='read_shop_item'),
    path('shop-items/<int:pk>/update/', shop_item_views.update_shop_item, name='update_shop_item'),
    path('shop-items/<int:pk>/delete/', shop_item_views.delete_shop_item, name='delete_shop_item'),

    path('purchases/', purchase_views.get_purchase, name='purchase_list'),
    path('purchases/create/<int:pk>/', purchase_views.create_purchase, name='create_purchase'),
    path('purchases/<int:pk>/', purchase_views.read_purchase, name='read_purchase'),
    path('purchases/<int:pk>/update/', purchase_views.update_purchase, name='update_purchase'),
    path('purchases/<int:pk>/delete/', purchase_views.delete_purchase, name='delete_purchase'),
]