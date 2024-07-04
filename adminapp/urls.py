from django.contrib import admin
from django.urls import path, include
from adminapp import views

urlpatterns = [
    path('adindex/', views.adindex, name='adindex'),

    path('contact/', views.contact, name='pages-contact'),
    path('error/', views.error, name='pages-error'),
    path('login/', views.loginview, name='pages-login'),
    path('register/', views.registerview, name='pages-register'),
    path('data/', views.data, name='tables-data'),
    path('general/', views.general, name='tables-general'),
    path('profile/', views.profile, name='users-profile'),

    #category
    path('category/', views.category, name='category'),
    path('delete/<int:id>', views.deleteview, name='delete'),
    path('edit/<int:id>', views.editview, name='edit'),
    path('update/<int:id>/', views.updateview, name='update'),

    #sub_category
    path('sub-category/', views.sub_category, name='sub-category'),
    path('sub-delete/<int:id>/', views.sub_delete, name='sub-delete'),
    path('sub-edit/<int:id>/', views.sub_edit, name='sub-edit'),
    path('sub-update/<int:id>/', views.sub_update, name='sub-update'),

    #colr
    path('color/', views.color, name='color'),
    path('color-delete/<int:id>/', views.color_delete, name='color-delete'),
    path('color-edit/<int:id>/', views.color_edit, name='color-edit'),
    path('color-update/<int:id>/', views.color_update, name='color-update'),


    #product
    path('product/', views.product, name='product'),
    path('pro-table/', views.pro_table, name='pro-table'),
    path('pro-delete/<int:id>/', views.pro_delete, name='pro-delete'),
    path('pro-edit/<int:id>/', views.pro_edit, name='pro-edit'),
    path('pro-update/<int:id>/', views.pro_update, name='pro-update'),


    #manage_user
    path('manage-user/', views.manage_user, name='manage_user'),
    path('manage-user-delete/<int:id>/', views.user_delete, name='manage-user-delete'),


    #order
    path('order/', views.order, name='order'),
    path('order-delete/<int:id>/', views.order_delete, name='order-delete'),
    path('order-detail/', views.order_detail, name='order-detail'),
]