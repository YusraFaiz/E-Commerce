from django.contrib import admin
from .models import Products,Order
# Register your models here.


admin.site.site_header = "E-Commerce Site"
admin.site.site_title = "Yusra Shopping"
admin.site.index_title = "Manage Yusra Shopping"

class ProductAdmin(admin.ModelAdmin):

    def change_category_to_default(self,request,queryset):
        queryset.update(category="default")
    change_category_to_default.short_description = 'Default Category'    
    list_display = ('title','price','discount_price','category','description','image',)
    search_fields = ['title',]
    actions = ('change_category_to_default',)
    list_editable = ('price',)
admin.site.register(Products,ProductAdmin)
admin.site.register(Order)