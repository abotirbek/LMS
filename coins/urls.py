from django.urls import path
from . import views

urlpatterns = [
    path('transactions/', views.get_coin_transaction, name='coin_transaction_list'),
    path('transactions/create/', views.create_coin_transaction, name='create_coin_transaction'),
    path('transactions/<int:pk>/', views.read_coin_transaction, name='read_coin_transaction'),
    path('transactions/<int:pk>/update/', views.update_coin_transaction, name='update_coin_transaction'),
    path('transactions/<int:pk>/delete/', views.delete_coin_transaction, name='delete_coin_transaction'),

    path('shop-items/', views.get_shop_item, name='shop_item_list'),
    path('shop-items/create/', views.create_shop_item, name='create_shop_item'),
    path('shop-items/<int:pk>/', views.read_shop_item, name='read_shop_item'),
    path('shop-items/<int:pk>/update/', views.update_shop_item, name='update_shop_item'),
    path('shop-items/<int:pk>/delete/', views.delete_shop_item, name='delete_shop_item'),

    path('purchases/', views.get_purchase, name='purchase_list'),
    path('purchases/create/', views.create_purchase, name='create_purchase'),
    path('purchases/<int:pk>/', views.read_purchase, name='read_purchase'),
    path('purchases/<int:pk>/update/', views.update_purchase, name='update_purchase'),
    path('purchases/<int:pk>/delete/', views.delete_purchase, name='delete_purchase'),
]