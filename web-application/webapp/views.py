import threading

from django.conf import settings
from django.core.mail import EmailMessage
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.utils.translation import ugettext_lazy as _
from django.views.generic import TemplateView, FormView, ListView

from catalog.models import Product, CategorySeason
from news.models import News
from webapp.forms import FeedbackForm
from webapp.models import *


class IndexListView(ListView):
    template_name = 'index.html'
    context_object_name = 'products'
    paginate_by = 10
    queryset = Product.objects.all()

    def get_context_data(self, **kwargs):
        context = super(IndexListView, self).get_context_data(**kwargs)
        context['advantages'] = Advantage.objects.all()[:3]
        context['seasons'] = CategorySeason.objects.all()
        context['about'] = About.objects.first()
        context['reviews'] = Review.objects.all()
        context['news'] = News.objects.order_by('-pub_date')[:6]
        context['banner'] = Banner.objects.first()
        return context


class PaymentAndDeliveryView(TemplateView):
    template_name = 'payment_and_delivery.html'

    def get_context_data(self, **kwargs):
        context = super(PaymentAndDeliveryView, self).get_context_data()
        context['payment_and_delivery'] = PaymentAndDelivery.objects.all()
        context['we_cooperate'] = WeCooperate.objects.first()
        context['partners'] = Partner.objects.all()
        return context


class ReviewView(TemplateView):
    template_name = 'reviews.html'

    def get_context_data(self, **kwargs):
        context = super(ReviewView, self).get_context_data(**kwargs)
        context['reviews'] = Review.objects.all()
        return context


class ContactView(TemplateView):
    template_name = 'contacts.html'

    def get_context_data(self, **kwargs):
        context = super(ContactView, self).get_context_data(**kwargs)
        context['contact'] = Contact.objects.first()
        context['coordinate'] = Coordinate.objects.first()
        return context


class FeedbackFormView(FormView):
    form_class = FeedbackForm
    template_name = 'index.html'

    def get_success_url(self):
        return self.request.META['HTTP_REFERER']

    def form_valid(self, form):
        feedback = form.save(commit=False)
        name = form.cleaned_data['name']
        phone = form.cleaned_data['phone']
        email = form.cleaned_data['email']
        if form.cleaned_data['message']:
            message = form.cleaned_data['message']
        else:
            message = ''
        feedback.save()
        thread = threading.Thread(target=self.send_email_feedback, args=(name, phone, email, message))
        thread.start()
        # return JsonResponse(dict(success=True, message='Успешно отпавлено'))
        return super(FeedbackFormView, self).form_valid(form)

    @staticmethod
    def send_email_feedback(name, phone, email, message):
        context = {
            'name': name,
            'phone': phone,
            'email': email,
            'message': message
        }

        content = render_to_string('send_mail/feedback.html', context)
        mail = EmailMessage(_('Обратная связь'), content, to=[settings.EMAIL_DEFAULT])
        mail.content_subtype = 'html'
        mail.send()
