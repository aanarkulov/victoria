from django.contrib import admin

from webapp.models import *


class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone')


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'city', 'image')


class PaymentAndDeliveryAdmin(admin.ModelAdmin):
    list_display = ('title',)
    prepopulated_fields = {'slug': ('title',)}


class ContactAdmin(admin.ModelAdmin):
    list_display = ('address', 'phone', 'email', 'operating_mode')


class CoordinateAdmin(admin.ModelAdmin):
    list_display = ('address', 'position')


admin.site.register(Banner)
admin.site.register(Feedback, FeedbackAdmin)
admin.site.register(ContactNumber)
admin.site.register(Advantage)
admin.site.register(About)
admin.site.register(Review, ReviewAdmin)
admin.site.register(LinkToSocialNetwork)
admin.site.register(PaymentAndDelivery, PaymentAndDeliveryAdmin)
admin.site.register(WeCooperate)
admin.site.register(Partner)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Coordinate, CoordinateAdmin)
