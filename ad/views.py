from django.shortcuts import render, redirect
from .forms import ProductForm
from .services import get_product_all, get_categories, get_one_product, category_product
from django.core.paginator import Paginator
from .models import Product
# Create your views here.


def home(request):
    category = get_categories()
    products_all = get_product_all()
    context = {
        'categories': category,
        'products': products_all
    }
    return render(request, 'index.html', context)


def details(request, slug):
    one_product = get_one_product(slug)
    ctx = {
        'products': one_product
    }
    return render(request, 'ads-details.html', ctx)


def post_ad(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            category = form.cleaned_data['category']
            price = form.cleaned_data['price']
            decription = form.cleaned_data['decription']
            phone_number = form.cleaned_data['phone_number']
            location = {"region": f"{form.cleaned_data['region']}", "district": f"{form.cleaned_data['city']}"}
            user = form.cleaned_data['user']

            if title and category and price and location and user:
                created = Product.objects.create(title=title, category=category, price=price, decription=decription, phone_number=phone_number, location=location,
                                                        user=user)
                return redirect('products')
    forms = ProductForm()
    ctx = {
      'forms': forms
    }
    return render(request, 'post-ads.html', ctx)


def products(request, ctg_slug=None):
    if ctg_slug:
        c_products = category_product(ctg_slug)
        print('>>>>>>>>>>>>>>>>>>>>>>>>>', c_products)
        paginator = Paginator(c_products, 10)  # Show 25 contacts per page.
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        page_count = paginator.num_pages
        page_l = []
        for i in range(1, page_count):
            page_l.append(i)
        category = get_categories()
    else:
        products = get_product_all()
        print('>>>>>>>>>>>>>>>>>>>>>>>>>', products)
        paginator = Paginator(products, 10)  # Show 25 contacts per page.
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        page_count = paginator.num_pages
        page_l = []
        for i in range(1, page_count):
            page_l.append(i)
        category = get_categories()

    context = {
        'products': page_obj,
        'category_name': category
    }
    return render(request, 'ads.html', context)

def one_category_home(request, ctg_slug):
    c_products = category_product(ctg_slug)
    print('>>>>>>>>>>>>>>>>>>>>>>>>>', c_products)
    context = {
        'products': c_products
    }
    return render(request, 'category_product.html', context)