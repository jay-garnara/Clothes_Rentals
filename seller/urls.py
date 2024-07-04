from django.contrib import admin
from django.urls import path, include
from seller import views


urlpatterns = [
    path('selindex/', views.selIndex, name='selindex'),
    path('blog/', views.Blog, name='blog'),
    path('blog-single/', views.Blog_Single, name='blog-single'),
    path('signup/', views.Signup, name='signup'),
    path('login/', views.Login, name='login'),
    path('shop/', views.Shop, name='shop'),
    path('checkout/', views.Checkout, name='checkout'),
    path('shop/<str:id>/', views.Product_Details, name='product-details'),
    path('contact-us/', views.Contact, name='contact-us'),
    path('place-order/', views.Place_Order, name='place-order'),
    path('search/', views.Search, name='search'),
    path('payment/', views.payment, name='payment'),

    #cart

    path('cart/add/<int:id>/', views.cart_add, name='cart_add'),
    path('cart/item_clear/<int:id>/', views.item_clear, name='item_clear'),
    path('cart/item_increment/<int:id>/', views.item_increment, name='item_increment'),
    path('cart/item_decrement/<int:id>/', views.item_decrement, name='item_decrement'),
    path('cart/cart_clear/', views.cart_clear, name='cart_clear'),
    path('cart/cart-detail/', views.cart_detail,name='cart_detail'),

    path('searchcate/<int:id>/', views.searchcate, name='searchcate'),
    path('searchcolor/<int:id>/', views.searchcolor, name='searchcolor'),
]