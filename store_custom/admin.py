from django.contrib import admin
from store.admin import ProductAdmin
from store.models import Product
from tags.models import TaggedItem
from django.contrib.contenttypes.admin import GenericTabularInline
# Register your models here.


class TagInLine(GenericTabularInline):
    model = TaggedItem
    autocomplete_fields = ['tag']
class CustomProductAdmin(ProductAdmin):
    inlines = [TagInLine]

admin.site.unregister(Product)
admin.site.register(Product,CustomProductAdmin)
