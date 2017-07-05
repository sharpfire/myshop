from django.contrib import admin

# Register your models here.

from shop.models import Product,Category

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name','slug']
    #我们使用 prepopulated_fields 属性来指定那些要使用其
    # 他字段来自动赋值的字段。
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Category, CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'stock',
                    'available', 'created', 'updated']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['price', 'stock', 'available']
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(Product,ProductAdmin)