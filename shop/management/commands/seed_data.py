import random
import decimal
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.utils.text import slugify
from shop.models import Category, Product, Order, OrderItem

User = get_user_model()

CATEGORIES = ['Electronics', 'Clothing', 'Books', 'Home and Garden', 'Sports']

PRODUCTS = [
    ('Wireless Headphones', 'Electronics', 79.99),
    ('Mechanical Keyboard', 'Electronics', 129.99),
    ('USB-C Hub', 'Electronics', 49.99),
    ('LED Desk Lamp', 'Electronics', 34.99),
    ('Smartphone Stand', 'Electronics', 19.99),
    ('Cotton T-Shirt', 'Clothing', 24.99),
    ('Running Shorts', 'Clothing', 34.99),
    ('Wool Sweater', 'Clothing', 89.99),
    ('Denim Jacket', 'Clothing', 119.99),
    ('Python Crash Course', 'Books', 39.99),
    ('Django for Professionals', 'Books', 44.99),
    ('Clean Code', 'Books', 35.99),
    ('The Pragmatic Programmer', 'Books', 42.99),
    ('Bamboo Cutting Board', 'Home and Garden', 29.99),
    ('Stainless Steel Water Bottle', 'Home and Garden', 22.99),
    ('Indoor Plant Pot Set', 'Home and Garden', 39.99),
    ('Yoga Mat', 'Sports', 49.99),
    ('Resistance Bands Set', 'Sports', 27.99),
    ('Jump Rope', 'Sports', 14.99),
    ('Foam Roller', 'Sports', 32.99),
]

STATUSES = ['pending', 'processing', 'shipped', 'delivered', 'cancelled']


class Command(BaseCommand):
    help = 'Seed the database with sample data'

    def handle(self, *args, **options):
        self.stdout.write('Clearing existing data...')
        OrderItem.objects.all().delete()
        Order.objects.all().delete()
        Product.objects.all().delete()
        Category.objects.all().delete()
        User.objects.filter(is_superuser=False).delete()

        # Superuser
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser(
                username='admin',
                email='admin@example.com',
                password='admin123',
            )

        # Categories
        categories = {}
        for name in CATEGORIES:
            cat = Category.objects.create(name=name, slug=slugify(name))
            categories[name] = cat
        self.stdout.write(f'Created {len(categories)} categories')

        # Products
        products = []
        for name, cat_name, price in PRODUCTS:
            p = Product.objects.create(
                name=name,
                slug=slugify(name),
                description=f'A great {name.lower()} for everyday use.',
                price=decimal.Decimal(str(price)),
                stock=random.randint(0, 100),
                category=categories[cat_name],
                is_active=True,
                is_published=True,
            )
            products.append(p)

        # 3 soft-deleted products
        for p in random.sample(products, 3):
            p.deleted_at = timezone.now()
            p.save()

        # 5 unpublished products
        published_products = [p for p in products if p.deleted_at is None]
        for p in random.sample(published_products, 5):
            p.is_published = False
            p.save()

        self.stdout.write(f'Created {len(products)} products')

        # Orders
        admin_user = User.objects.get(username='admin')
        order_count = 0
        for _ in range(10):
            items_sample = random.sample(products, random.randint(2, 4))
            total = sum(item.price * random.randint(1, 3) for item in items_sample)
            order = Order.objects.create(
                user=admin_user,
                status=random.choice(STATUSES),
                total=total,
            )
            for product in items_sample:
                qty = random.randint(1, 3)
                OrderItem.objects.create(
                    order=order,
                    product=product,
                    quantity=qty,
                    price=product.price,
                )
            order_count += 1

        self.stdout.write(f'Created {order_count} orders')
        self.stdout.write(self.style.SUCCESS(
            f'\nDone! Created {len(categories)} categories, {len(products)} products, {order_count} orders.'
        ))
