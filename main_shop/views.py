from django.shortcuts import render, get_object_or_404
from main_shop.models import Category, Product


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)

    return render(request, 'shop/list.html', {
        'category': category,
        'categories': categories,
        'products': products
    })


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    return render(request, 'shop/detail.html', {'product': product})


from django.shortcuts import redirect, get_object_or_404
from .models import Product  # Припустимо, у вас модель називається Product


def add_to_cart(request, product_id):
    # Отримуємо або створюємо кошик у сесії користувача
    cart = request.session.get('cart', {})

    # Перетворюємо id в рядок, бо ключі в сесії (JSON) мають бути рядками
    product_id_str = str(product_id)

    if product_id_str in cart:
        cart[product_id_str] += 1
    else:
        cart[product_id_str] = 1

    # Зберігаємо оновлений кошик назад у сесію
    request.session['cart'] = cart

    # Повертаємо користувача на ту сторінку, де він був
    return redirect(request.META.get('HTTP_REFERER', 'main_shop:product_list'))


def product_list(request):
    # Ваш існуючий код (отримання товарів тощо)
    products = Product.objects.all()

    # Рахуємо загальну кількість штук у кошику
    cart = request.session.get('cart', {})
    cart_total_items = sum(cart.values()) if cart else 0

    return render(request, 'shop/list.html', {
        'products': products,
        'cart_total_items': cart_total_items,  # Передаємо у шаблон
        # ваші інші змінні (categories тощо)
    })


from django.shortcuts import render
from .models import Product  # Перевірте назву вашої моделі товарів


def cart_detail(request):
    cart = request.session.get('cart', {})
    cart_products = []
    total_price = 0

    # Отримуємо об'єкти товарів із бази даних на основі ID з кошика
    if cart:
        # Перетворюємо ключі (рядки) назад у числа для запиту до БД
        product_ids = [int(pid) for pid in cart.keys()]
        products = Product.objects.filter(id__in=product_ids)

        for product in products:
            quantity = cart[str(product.id)]
            # Припустимо, у вашій моделі Product є поле price
            item_total = product.price * quantity
            total_price += item_total

            # Додаємо тимчасові змінні до об'єкта, щоб зручно вивести в шаблоні
            product.quantity = quantity
            product.total_price = item_total
            cart_products.append(product)

    return render(request, 'shop/cart.html', {
        'cart_products': cart_products,
        'total_price': total_price
    })