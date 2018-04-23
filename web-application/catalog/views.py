import threading
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from django.core.mail import EmailMessage
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.views.generic import DetailView, ListView, FormView, CreateView

from catalog.filters import ProductFilters
from catalog.forms import OrderForm
from catalog.models import *


class CatalogListView(ListView):
    template_name = 'catalog/catalog.html'
    context_object_name = 'products'
    model = Product
    filterset_class = ProductFilters

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product_filter = self.filterset_class(self.request.GET, queryset=self.model.objects.all())
        context['product_filter'] = product_filter
        context['about_our_trousers'] = AboutOurTrousers.objects.first()
        return context


class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super(ProductDetailView, self).get_context_data(**kwargs)
        context['order_form'] = OrderForm(self.request.POST)
        return context


class OrderFormView(CreateView):
    model = OrderOfProduct
    form_class = OrderForm
    template_name = 'catalog/product.html'

    # context_object_name = 'order_form'

    def get_success_url(self):
        return self.request.META['HTTP_REFERER']

    def form_valid(self, form):
        oder_of_product = form.save(commit=False)
        name = form.cleaned_data['name']
        phone = form.cleaned_data['phone']
        email = form.cleaned_data['email']
        product = form.cleaned_data['id_product']
        product_obj = Product.objects.get(id=product)
        color = form.cleaned_data['color']
        quantity = form.cleaned_data['quantity']
        total_amount = str(quantity * product_obj.amount)
        oder_of_product.total_amount = total_amount
        oder_of_product.save()
        thread = threading.Thread(target=self.send_email_order,
                                  args=(name, phone, email, product, color, quantity, total_amount))
        thread.start()

        return JsonResponse(dict(success=True, message='Заказ успешно отправлено'))

    def form_invalid(self, form):
        return JsonResponse(dict(success=False, message='Form invalid'))

    @staticmethod
    def send_email_order(name, phone, email, product, color, quantity, total_amount):
        context = {
            'name': name,
            'phone': phone,
            'email': email,
            'id_product': product,
            'color': color,
            'quantity': quantity,
            'total_amount': total_amount,
        }

        content = render_to_string('send_mail/order_of_product.html', context)
        mail = EmailMessage(_('Заказы'), content, to=[settings.EMAIL_DEFAULT])
        mail.content_subtype = 'html'
        mail.send()
