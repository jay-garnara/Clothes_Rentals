from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import login, logout, authenticate
from seller.models import *
from seller.forms import *
import os
from django import forms
from django.contrib.auth.models import User




# Create your views here.
def adindex(request):
    item = Product.objects.all()
    order = OrderItem.objects.all()
    customer = User.objects.all().count()
    product = Product.objects.all().count()
    cate = Category.objects.all().count()

    context = {
        'item': item,
        'order': order,
        'customer': customer,
        'product': product,
        'cate': cate,
    }
    return render(request, 'admin/adindex.html', context=context)


def contact(request):
    return render(request, 'admin/pages-contact.html')


def error(request):
    return render(request, 'admin/pages-error.html')


def loginview(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(adindex)
        else:
            print("user not found")
    return render(request, 'admin/pages-login.html')


def registerview(request):
    if request.method == "POST":
        if request.POST.get('password') == request.POST.get('password1'):
            try:
                User.objects.get(username=request.POST.get('username'))
                return HttpResponse('Usealready exixist')
            except User.DoesNotExist:
                User.objects.create_user(username=request.POST.get('username'), first_name=request.POST.get('name'), email=request.POST.get('email'), password=request.POST.get('password'))
                return redirect(loginview)
        else:
            return HttpResponse('Password not match')
    return render(request, 'admin/pages-register.html')


def data(request):
    colors = Color.objects.all()

    context = {
        'colors': colors,
    }

    return render(request, 'admin/tables-data.html', context=context)


def general(request):
    cate = Category.objects.all()
    sub_cate = Sub_Category.objects.all()
    context = {
        'cate': cate,
        'sub_cate': sub_cate,
    }
    return render(request, 'admin/tables-general.html', context=context)


def profile(request):
    return render(request, 'admin/users-profile.html')


def category(request):
    if request.method == "POST":
        form = categoryform(request.POST)
        if form.is_valid():
            form.save()
            return redirect(general)
        else:
            print(form.errors)
            print("errors")
    return render(request, 'admin/category.html')

def deleteview(request, id):
    cate = Category.objects.get(id=id)
    cate.delete()
    return redirect(general)

def editview(request, id):
    cate = Category.objects.get(id=id)
    context = {
        'cate': cate,
    }
    return render(request, 'admin/edit.html', context=context)


def updateview(request, id):
    if request.method == "POST":
        cate = Category.objects.get(id=id)
        form = categoryform(request.POST, instance=cate)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
            print("errors")
    return render(request, 'admin/edit.html')

# <!-- ======= Start Sub Category ======= -->
def sub_category(request):
    cate = Category.objects.all()
    if request.method == "POST":
        form = subcategoryform(request.POST)
        if form.is_valid():
            form.save()
            return redirect(general)
        else:
            print(form.errors)
            print("errors")
    return render(request, 'admin/sub-category.html', context={'cate': cate})


def sub_delete(request, id):
    sub_cate = Sub_Category.objects.get(id=id)
    sub_cate.delete()
    return redirect(general)

def sub_edit(request, id):
    sub_cate = Sub_Category.objects.get(id=id)
    cate = Category.objects.all()
    context = {
        'cate': cate,
        'sub_cate': sub_cate,
    }
    return render(request, 'admin/cate-edit.html', context=context)

def sub_update(request, id):
    if request.method == "POST":
        sub_cate = Sub_Category.objects.get(id=id)
        form = subcategoryform(request.POST, instance=sub_cate)
        if form.is_valid():
            form.save()
            return redirect(general)
        else:
            print(form.errors)
            print("errors")
    return render(request, 'admin/cate-edit.html')

# <!-- ======= End Sub Category ======= -->


# <!-- ======= Color ======= -->
def color(request):
    if request.method == "POST":
        form = colorform(request.POST)
        if form.is_valid():
            form.save()
            return redirect(data)
        else:
            print(form.errors)
            print("errors")
    return render(request, 'admin/color.html')

def color_delete(request, id):
    colors = Color.objects.get(id=id)
    colors.delete()
    return redirect(data)

def color_edit(request, id):
    colors = Color.objects.get(id=id)

    context = {
        'colors': colors,
    }
    return render(request, 'admin/color-edit.html', context=context)


def color_update(request, id):
    if request.method == "POST":
        colors = Color.objects.get(id=id)
        form = colorform(request.POST, instance=colors)
        if form.is_valid():
            form.save()
            return redirect(data)
        else:
            print(form.errors)
            print("errors")
    return render(request, 'admin/color-edit.html')

# <!-- ======= Start Product ======= -->

def pro_table(request):
    product = Product.objects.all()

    context = {
        'product': product,
    }
    return render(request, 'admin/pro-table.html', context=context)


def product(request):
    cate = Category.objects.all()
    sub_cate = Sub_Category.objects.all()
    colors = Color.objects.all()


    if request.method == "POST":
        form = productform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse("Data added")
        else:
            print(form.errors)
            print("errors")

    context = {
        'cate': cate,
        'sub_cate': sub_cate,
        'colors': colors,
    }
    return render(request, 'admin/product.html', context=context)

def pro_delete(request, id):
    product = Product.objects.get(id=id)
    product.delete()
    return redirect(pro_table)


def pro_edit(request, id):
    product = Product.objects.get(id=id)
    cate = Category.objects.all()
    sub_cate = Sub_Category.objects.all()
    colors = Color.objects.all()
    context = {
        'product': product,
        'cate': cate,
        'sub_cate': sub_cate,
        'colors': colors,
    }
    return render(request, 'admin/pro-edit.html', context=context)


def pro_update(request, id):
    cate = Category.objects.all()
    sub_cate = Sub_Category.objects.all()
    colors = Color.objects.all()

    if request.method == "POST":
        product = Product.objects.get(id=id)
        form = productform(request.POST, request.FILES, instance=product)
        if len(request.FILES) != 0:
            if len(product.image) > 0:
                os.remove(product.image.path)
            product.image = request.FILES['image']
        if form.is_valid():
            form.save()
            return redirect(pro_table)
        else:
            print(form.errors)
            print("errors")

    context = {
        'cate': cate,
        'sub_cate': sub_cate,
        'colors': colors,
    }
    return render(request, 'admin/pro-edit.html', context=context)

# <!-- ======= End Product ======= -->



# <!-- ======= Start Manage User ======= -->
def manage_user(request):
    staff = User.objects.all()

    context = {
        'staff': staff,
    }
    return render(request, 'admin/manage_user.html', context=context)

def user_delete(request,id):
    staff = User.objects.get(id=id)
    staff.delete()
    return redirect(manage_user)

# <!-- ======= End Manage User ======= -->


# <!-- ======= Start Order ======= -->

def order(request):
    orders = OrderItem.objects.all()

    context = {
        'orders': orders,
    }
    return render(request, 'admin/order.html', context=context)


def order_delete(request, id):
    orders = OrderItem.objects.get(id=id)
    orders.delete()
    return redirect(order)


def order_detail(request):
    detail = OrderItem.objects.all()

    context = {
        'detail': detail
    }
    return render(request, 'admin/order-detail.html', context=context)