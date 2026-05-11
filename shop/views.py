from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.http.response import HttpResponse, JsonResponse
from .models import Product, Order, Category

User = get_user_model()



# readers edit this function body to test any utility
# then visit http://127.0.0.1:8000/test/
def test_view(request):
    return JsonResponse({"result": "done"})


# index page with some default stats
def index(request):
    categories = [
        "utils/query.py",
        "utils/models.py", 
        "utils/managers.py",
        "utils/views.py",
        "utils/forms.py",
        "utils/serializers.py",
        "utils/validators.py",
        "utils/files.py",
        "utils/dates.py",
        "utils/urls.py",
        "utils/cache.py",
        "utils/services.py",
        "utils/security.py",
        "utils/logging.py",
        "utils/testing.py",
        "utils/admin.py",
        "utils/templates.py",
    ]
    return render(request, "index.html", {
        "total_products": Product.objects.count(),
        "total_orders": Order.objects.count(),
        "total_categories": Category.objects.count(),
        "total_users": User.objects.count(),
        "categories": categories,
    })


