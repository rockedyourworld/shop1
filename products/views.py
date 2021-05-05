from django.views.generic import ListView

from products.models import ProductModel


class ProductListView(ListView):
    template_name = 'products.html'
    queryset = ProductModel.objects.order_by('-pk')
