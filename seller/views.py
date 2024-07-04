from django.shortcuts import render, HttpResponse, redirect
from . import models
from . import forms
from django.contrib.auth.models import User
from seller.models import Category, Product, Order, OrderItem, Color
from django.contrib.auth import login, logout, authenticate
from django.core.paginator import Paginator
from django.db.models import Q
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required



# from django.contrib.auth.decorators import login_required
from cart.cart import Cart


# Create your views here.
def selIndex(request):
    category = Category.objects.all()
    colors = Color.objects.all()
    if request.method == "POST":
        min = request.POST.get('min_price')
        max = request.POST.get('max_price')
        print("min valuessss",min)
        range_prod = Product.objects.filter(price__gte=min).filter(price__lte=max)[:10]
        print("product",range_prod)
        context = {
            'category': category,
            'product_range': range_prod,
            'colors': colors,
        }
    else:
        product = Product.objects.all()[:10]
        context = {
            'category': category,
            'product': product,
            'colors': colors,
        }
    return render(request, 'selindex.html', context=context)


def Blog(request):
    return render(request, 'blog.html')


def Blog_Single(request):
    return render(request, 'blog.html')


def Shop(request):
    category = Category.objects.all()
    colors = Color.objects.all()
    product = Product.objects.all()
    paginator = Paginator(product, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    totalpage = page_obj.paginator.num_pages

    context = {
        'category': category,
        'colors': colors,
        'product': page_obj,
        'page_obj': page_obj,
        'lastpage': totalpage,
        'totalPagelist': [n + 1 for n in range(totalpage)]
    }
    return render(request, 'shop.html', context=context)


def Checkout(request):
    return render(request, 'checkout.html')


def Place_Order(request):
    if request.method == "POST":
        uid = request.session.get('_auth_user_id')
        user = User.objects.get(id=uid)
        cart = request.session.get('cart')
        print(cart)

        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        country = request.POST.get('country')
        state = request.POST.get('state')
        zip = request.POST.get('zip')
        amount = request.POST.get('amount')

        order_id = request.POST.get('order_id')
        payment = request.POST.get('payment')

        print(firstname)

        #print(user, firstname, lastname, email, address, phone, country, state, zip, order_id, payment, amount)

        order = Order(
            user=user,
            firstname=firstname,
            lastname=lastname,
            email=email,
            address=address,
            phone=phone,
            country=country,
            state=state,
            zip=zip,
            amount=amount
        )
        if order.phone == '':
            order.phone = None
        if zip == '':
            zip = None
        order.zip = zip
        order.save()

        final_total = 0
        fnl = models.FinalOrder.objects.create(user=request.user,total=0)

        for i in cart:

            a = int(cart[i]['price'])
            b = int(cart[i]['quantity'])

            total = a * b
            final_total += total
            #product_instance = Product.objects.get(name=cart[i]['name'])

            product_instance = Product.objects.get(id=cart[i]['product_id'])

            item = OrderItem(
                user=request.user,
                final = fnl,
                order=order,
                product=product_instance,  #cart[i]['name'],
                image =cart[i]['image'],
                quantity=cart[i]['quantity'],
                price=cart[i]['price'],
                total=total
            )
            item.save()

        fnl.total = final_total
        fnl.save()

    return render(request, 'place-order.html')


def Product_Details(request,id):
    product = Product.objects.filter(id=id).first()

    context = {
        'product': product,
    }
    return render(request, 'product-details.html', context=context)


# def Cart_Details(request):
#     return render(request, 'cart/cart-details')

def Contact(request):
    form = forms.contactform(request.POST)
    if request.method == "POST":
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
            print("errors")
    return render(request, 'contact-us.html')


def Signup(request):
    if request.method == "POST":
        if request.POST.get('password') == request.POST.get('password1'):
            try:
                User.objects.get(username=request.POST.get('username'))
                return HttpResponse('Useralready exixist')
            except User.DoesNotExist:
                User.objects.create_user(username=request.POST.get('username'),
                                         first_name=request.POST.get('first_name'), email=request.POST.get('email'),
                                         password=request.POST.get('password'))
                # return HttpResponse('register succesfully')
                return redirect(Login)
        else:
            return HttpResponse('Password not match')
    return render(request, 'signup.html')


def Login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(selIndex)
        else:
            print("user not found")
    return render(request, 'login.html')


@login_required(login_url="login")
def cart_add(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("selindex")


# @login_required(login_url="")
def item_clear(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product)
    return redirect(cart_detail)


# @login_required(login_url="")
def item_increment(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect(cart_detail)


# @login_required(login_url="")
def item_decrement(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.decrement(product=product)
    return redirect(cart_detail)


# @login_required(login_url="")
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect(cart_detail)


# @login_required(login_url="")
def cart_detail(request):
    return render(request, 'cart/cart_detail.html')


def searchcate(request, id):
    category = Category.objects.all()
    colors = Color.objects.all()
    sub_cat = models.Sub_Category.objects.get(id=id)
    print(sub_cat)
    prod = models.Product.objects.filter(sub_category=sub_cat)
    print(prod)
    context = {'product': prod,
               'category': category,
               'colors': colors,
               }
    return render(request, 'shop.html', context=context)


def searchcolor(requesst, id):
    category = Category.objects.all()
    colors = Color.objects.all()
    color = models.Color.objects.get(id=id)

    clr = models.Product.objects.filter(color=color)

    context = {
        'colors': colors,
        'product': clr,
        'category': category,
    }

    return render(requesst, 'shop.html', context=context)


def Search(request):
    if 'query' in request.GET:
        query = request.GET.get('query', 'default-value')
        multi = Q(Q(name__icontains=query) | Q(price__icontains=query))
        product = Product.objects.filter(multi)
    else:
        product = Product.objects.all()

    context = {
        'product': product,
    }
    return render(request, 'search.html', context=context)


def payment(request):
    return render(request, 'payment.html')