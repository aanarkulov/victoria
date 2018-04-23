from django.http import JsonResponse
from django.views.generic import ListView, DetailView, FormView

from news.forms import SubscriberForm
from news.models import News, Subscriber


class NewsListView(ListView):
    template_name = 'news/news.html'
    model = News
    context_object_name = 'news'

    # paginate_by = 6

    def get_queryset(self):
        return News.objects.order_by('-pub_date')

    # def get_queryset(self):
    #     if self.request.is_ajax():
    #         self.template_name = 'object.html'

    # def get_context_data(self, **kwargs):
    #     context = super(NewsListView, self).get_context_data(**kwargs)
    # pagination = Paginator()
    # return context


class NewsDetailView(DetailView):
    model = News
    template_name = 'news/detail_of_news.html'
    context_object_name = 'new'


class SubscriberFormView(FormView):
    form_class = SubscriberForm

    def form_valid(self, form):
        try:
            Subscriber.objects.get(email=form.cleaned_data['email'])
            return JsonResponse(dict(success=False, message='Вы уже подписались на рассылку'))
        except:
            form.save()
            return JsonResponse(dict(success=True, message='Вы успешно подписались на рассылку'))