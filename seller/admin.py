from django.contrib import admin

from .models import *

# Register your models here.

class OrderItemTubeleinline(admin.TabularInline):
    model = OrderItem

class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderItemTubeleinline]

admin.site.register(Category)
admin.site.register(Sub_Category)
admin.site.register(Color)
admin.site.register(Product)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem)


class Contact_usAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'message']

admin.site.register(Contact_us, Contact_usAdmin)