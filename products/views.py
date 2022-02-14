from django.shortcuts import render


def index(request):
    context = {'title': 'GeekShop'}
    return render(request, 'products/index.html', context)


def products(request):
    context = {
        'title': 'GeekShop products',
        'products': [
            {
                'name': 'Худи черного цвета с монограммами adidas Originals',
                'price': '6 090,00 руб.',
                'description': 'Мягкая ткань для свитшотов. Стиль и комфорт – это образ жизни.',
                'filepath': 'vendor/img/products/Adidas-hoodie.png'
            },
            {
                'name': 'Синяя куртка The North Face',
                'price': '23 725,00 руб.',
                'description': 'Гладкая ткань. Водонепроницаемое покрытие. Легкий и теплый пуховый наполнитель.',
                'filepath': 'vendor/img/products/jacket.png'
            },
            {
                'name': 'Коричневый спортивный oversized-топ ASOS DESIGN',
                'price': '3 390,00 руб.',
                'description': 'Материал с плюшевой текстурой. Удобный и мягкий.',
                'filepath': 'vendor/img/products/oversized-top.png'
            },
            {
                'name': 'Черный рюкзак Nike Heritage',
                'price': '2 340,00 руб.',
                'description': 'Плотная ткань. Легкий материал.',
                'filepath': 'vendor/img/products/backpack.png'
            },
            {
                'name': 'Черные туфли на платформе с 3 парами люверсов Dr Martens 1461 Bex',
                'price': '13 590,00 руб.',
                'description': 'Гладкий кожаный верх. Натуральный материал.',
                'filepath': 'vendor/img/products/shoes.png'

            },
            {
                'name': 'Темно-синие широкие строгие брюки ASOS DESIGN',
                'price': '2 890,00 руб.',
                'description': 'Легкая эластичная ткань сирсакер Фактурная ткань.',
                'filepath': 'vendor/img/products/trousers.png'
            }
        ],
    }

    return render(request, 'products/products.html', context)