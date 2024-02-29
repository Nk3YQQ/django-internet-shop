from django.shortcuts import render, redirect

from shopapp.models import Category, Product


def index(request):
    return render(request, 'shopapp/index.html')


def categories(request):
    context = {
        "object_list": Category.objects.all()
    }
    return render(request, 'shopapp/categories.html', context)


def get_good(request, pk):
    object_1 = Product.objects.get(pk=pk)
    category_object = Category.objects.get(pk=object_1.category_id)
    context = {
        "object": object_1,
        "category_object": category_object
    }
    return render(request, 'shopapp/good.html', context)


def get_all_goods(request):
    name = request.GET.get("query")
    if name:
        object_list = Product.objects.filter(name__icontains=name)
    else:
        object_list = Product.objects.all()
    context = {
        "object_list": object_list
    }
    return render(request, "shopapp/goods.html", context)


def get_category(request):
    category_id = request.GET.get('category')
    products = Product.objects.filter(category_id=category_id)
    context = {
        "object_list": products
    }
    return render(request, "shopapp/filter_goods.html", context)


def add_product(request):
    categories_list = Category.objects.all()
    context = {
        "object_list": categories_list
    }
    if request.method == "POST":
        category = request.POST.get("category")
        content = request.POST.get("content")
        image = request.FILES.get("image")
        if not content:
            content = ''
        category_name = Category.objects.get(name=category)
        Product.objects.create(
            name=request.POST.get("name"),
            content=content,
            image=image,
            category=category_name,
            amount=request.POST.get("amount")

        )
        return redirect('all_categories')
    return render(request, "shopapp/add_product.html", context)
