from django.utils import timezone

from news.forms import SubscriberForm
from webapp.forms import FeedbackForm
from webapp.models import ContactNumber, LinkToSocialNetwork


def getting_different_info(request):
    contact_number = ContactNumber.objects.first()
    contact_numbers = ContactNumber.objects.all()
    link_to_social_networks = LinkToSocialNetwork.objects.first()
    year = timezone.now()
    feedback_form = FeedbackForm()
    subscriber_form = SubscriberForm()
    return locals()
