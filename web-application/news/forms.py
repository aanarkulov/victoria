from django import forms

from news.models import Subscriber, News


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        exclude = ('slug', 'created')

    send_to_subscribers = forms.BooleanField()


class SubscriberForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        fields = ('email',)