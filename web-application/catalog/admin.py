from django.contrib import admin

from catalog.models import *


class CategoryTypeAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    prepopulated_fields = {'slug': ('title',)}


class CategorySizeAdmin(admin.ModelAdmin):
    list_display = ('size', 'slug')
    prepopulated_fields = {'slug': ('size',)}


class ProductColorsAdmin(admin.ModelAdmin):
    list_display = ('name', 'color')


class CategorySeasonAdmin(admin.ModelAdmin):
    list_display = ('season', 'image')


class ProductImagesInline(admin.TabularInline):
    model = ProductImages
    extra = 0


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug', 'added_to')
    prepopulated_fields = {'slug': ('name',)}
    fieldsets = [
        (None, {'fields': ['type', 'size', 'season', 'color', 'name', 'slug', 'description', 'amount', 'currency',
                           'fabric_structure', 'weight_of_1_line', 'in_the_1st_line', 'action', 'popular', 'create_at']}),
    ]
    inlines = [ProductImagesInline]


# class ProductImagesAdmin(admin.ModelAdmin):
# list_display = ('product', 'image')


admin.site.register(CategoryType, CategoryTypeAdmin)
admin.site.register(CategorySize, CategorySizeAdmin)
admin.site.register(ProductColors, ProductColorsAdmin)
admin.site.register(Product, ProductAdmin)
# admin.site.register(ProductImages, ProductImagesAdmin)
admin.site.register(CategorySeason, CategorySeasonAdmin)
# admin.site.register(Descriptions)
admin.site.register(AboutOurTrousers)
admin.site.register(OrderOfProduct)
