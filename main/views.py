from django.shortcuts import render, redirect, get_object_or_404
from main.forms import ProductForm
from main.models import Product
from django.http import HttpResponse
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.utils.html import strip_tags

@login_required(login_url='/login')
def show_main(request):
    filter_type = request.GET.get("filter", "all")  # default 'all'
    category_filter = request.GET.get("category", "")  # category filter

    # Start with base query
    if filter_type == "all":
        product_list = Product.objects.all()
    else:
        product_list = Product.objects.filter(user=request.user)
    
    # Apply category filter if specified
    if category_filter:
        product_list = product_list.filter(category=category_filter)
    
    # Prepare context with filter information
    filter_message = ""
    if category_filter:
        category_display = dict(Product.CATEGORY_CHOICES).get(category_filter, category_filter)
        filter_message = f"Showing products in category: {category_display}"
        if filter_type == "my":
            filter_message = f"Showing your products in category: {category_display}"

    context = {
        'name': request.user.username,
        'class': 'PBP B',
        'product_list': product_list,
        'nama_aplikasi': 'Mustard Sports',
        'last_login': request.COOKIES.get('last_login', 'Never'),
        'category_filter': category_filter,
        'filter_message': filter_message,
        'filter_type': filter_type,
    }

    return render(request, "main.html", context)

def add_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == 'POST':
        product_entry = form.save(commit = False)
        product_entry.user = request.user
        product_entry.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "add_product.html", context)

@login_required(login_url='/login')
def show_product(request, id):
    product = get_object_or_404(Product, pk=id)

    context = {
        'product': product,
        'id': id,
        'nama_aplikasi': 'Mustard Sports',
        'user': request.user,
    }

    return render(request, "product_detail.html", context)

def show_xml(request):
     product_list = Product.objects.all()
     xml_data = serializers.serialize("xml", product_list)
     return HttpResponse(xml_data, content_type="application/xml")
 
def show_json(request):
    # Get filter parameters (same logic as show_main)
    filter_type = request.GET.get("filter", "all")
    category_filter = request.GET.get("category", "")

    # Start with base query
    if filter_type == "all":
        product_list = Product.objects.all()
    else:
        product_list = Product.objects.filter(user=request.user)
    
    # Apply category filter if specified
    if category_filter:
        product_list = product_list.filter(category=category_filter)
    
    data = [
        {
            'id': str(product.id),
            'name': product.name,
            'price': product.price,
            'description': product.description,
            'category': product.category,
            'thumbnail': product.thumbnail,
            'is_featured': product.is_featured,
            'user_id': product.user.id if product.user else None,
        }
        for product in product_list
    ]
    
    return JsonResponse(data, safe=False)

def show_xml_by_id(request, product_id):
   try:
       product_item = Product.objects.filter(pk=product_id)
       xml_data = serializers.serialize("xml", product_item)
       return HttpResponse(xml_data, content_type="application/xml")
   except Product.DoesNotExist:
       return HttpResponse(status=404)

def show_json_by_id(request, product_id):
    try:
        product = Product.objects.select_related('user').get(pk=product_id)
        data = {
            'id': str(product.id),
            'name': product.name,
            'price': product.price,
            'description': product.description,
            'category': product.category,
            'thumbnail': product.thumbnail,
            'is_featured': product.is_featured,
            'user_id': product.user_id,
            'user_username': product.user.username if product.user_id else None,
        }
        return JsonResponse(data)
    except Product.DoesNotExist:
        return JsonResponse({'detail': 'Not found'}, status=404)
   
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, f'Welcome to Mustard Sports, {user.username}! Your account has been created successfully.')
            return redirect('main:login')
        else:
            messages.error(request, 'Please correct the errors below and try again.')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f'Welcome back, {user.username}!')
            response = HttpResponseRedirect(reverse("main:show_main") + '?login=success')
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.error(request, 'Invalid username or password. Please try again.')

    else:
        form = AuthenticationForm(request)
    context = {'form': form}
    return render(request, 'login.html', context)

def logout_user(request):
    username = request.user.username if request.user.is_authenticated else 'User'
    logout(request)
    messages.success(request, f'Goodbye, {username}! You have been logged out successfully.')
    response = HttpResponseRedirect(reverse('main:login') + '?logout=success')
    response.delete_cookie('last_login')
    return response

def edit_product(request, id):
    product = get_object_or_404(Product, pk=id)
    form = ProductForm(request.POST or None, instance=product)
    if form.is_valid() and request.method == 'POST':
        form.save()
        return redirect('main:show_main')

    context = {
        'form': form
    }

    return render(request, "edit_product.html", context)

def delete_product(request, id):
    product = get_object_or_404(Product, pk=id)
    product_name = product.name
    product.delete()
    messages.success(request, f'Product "{product_name}" has been successfully deleted.')
    return HttpResponseRedirect(reverse('main:show_main') + '?delete=success')

@csrf_exempt
@require_POST
def add_product_entry_ajax(request):
    try:
        name = strip_tags(request.POST.get("name"))  # strip HTML tags!
        price = request.POST.get("price")
        description = strip_tags(request.POST.get("description"))  # strip HTML tags!
        category = request.POST.get("category")
        thumbnail = strip_tags(request.POST.get("thumbnail"))  # strip HTML tags!
        is_featured = request.POST.get("is_featured") == 'on'  # checkbox handling
        user = request.user

        # Validate required fields
        if not name or not price or not description:
            return JsonResponse({
                'status': 'error',
                'message': 'Name, price, and description are required fields.'
            }, status=400)

        # Validate price is a number
        try:
            price = float(price)
        except (ValueError, TypeError):
            return JsonResponse({
                'status': 'error',
                'message': 'Price must be a valid number.'
            }, status=400)

        new_product = Product(
            name=name, 
            price=price,
            description=description,
            category=category,
            thumbnail=thumbnail,
            is_featured=is_featured,
            user=user
        )
        new_product.save()

        return JsonResponse({
            'status': 'success',
            'message': 'Product created successfully!',
            'product_id': str(new_product.id)
        }, status=201)

    except Exception as e:
        return JsonResponse({
            'status': 'error',
            'message': f'An error occurred: {str(e)}'
        }, status=500)

@csrf_exempt
@require_POST
def edit_product_entry_ajax(request, id):
    try:
        product = get_object_or_404(Product, pk=id, user=request.user)
        
        # Validate required fields
        name = strip_tags(request.POST.get("name"))  # strip HTML tags!
        price = request.POST.get("price")
        description = strip_tags(request.POST.get("description"))  # strip HTML tags!
        
        if not name or not price or not description:
            return JsonResponse({
                'status': 'error',
                'message': 'Name, price, and description are required fields.'
            }, status=400)

        # Validate price is a number
        try:
            price = float(price)
        except (ValueError, TypeError):
            return JsonResponse({
                'status': 'error',
                'message': 'Price must be a valid number.'
            }, status=400)

        category = request.POST.get("category")
        thumbnail = strip_tags(request.POST.get("thumbnail"))  # strip HTML tags!
        is_featured = request.POST.get("is_featured") == 'on'  # checkbox handling

        product.name = name
        product.price = price
        product.description = description
        product.category = category
        product.thumbnail = thumbnail
        product.is_featured = is_featured
        product.save()

        return JsonResponse({
            'status': 'success',
            'message': 'Product updated successfully!',
            'product_id': str(product.id)
        }, status=200)
        
    except Product.DoesNotExist:
        return JsonResponse({
            'status': 'error',
            'message': 'Product not found or you do not have permission to edit it.'
        }, status=404)
    except Exception as e:
        return JsonResponse({
            'status': 'error',
            'message': f'An error occurred: {str(e)}'
        }, status=500)