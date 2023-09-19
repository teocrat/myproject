from django.contrib import admin
from . models import Author, Post, Buyer, Products, Orders, GameModel


class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name', 'surname']
    ordering = ['surname']
    list_filter = ['surname']

    fieldsets = [
        (
            None,
            {
                'classes': ['wide'],
                'fields': ['name', 'surname'],
            }
        ),
        ('Подробности',
            {
                'classes': ['collapse'],
                'description': 'Биография автора и дата его рождения',
                'fields': ['biography', 'bd'],
            },
         ),
        (
            'Email',
            {
                'fields': ['email'],
            }
        ),
    ]


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'category']
    ordering = ['title']
    list_filter = ['category']
    search_fields = ['surname']
    search_help_text = 'Search by Surname field'
    fields = ['title', 'post', 'author', 'category', 'viewed', 'published']


class BuyerAdmin(admin.ModelAdmin):
    list_display = ['name', 'reg_data']
    ordering = ['name']
    list_filter = ['reg_data']
    search_fields = ['name']
    search_help_text = 'Search by Name field'
    fieldsets = [
        (
            None,
            {
                'classes': ['wide'],
                'fields': ['name'],
            }
        ),
        ('Подробности',
            {
                'classes': ['collapse'],
                'description': 'Email покупателя, адрес и его телефон',
                'fields': ['email', 'address', 'phone'],
            },
         ),
    ]

class OrdersAdmin(admin.ModelAdmin):
    list_display =  ['client', 'order_date']
    ordering = ['order_date']
    search_fields = ['client']
    search_help_text = 'Search by Client field'
    list_filter = ['order_date']
    filds = ['client', 'product', 'sum_order', 'order_date']


class ProductsAdmin(admin.ModelAdmin):
    list_display = ['product_name', 'description', 'price', 'amount']
    ordering = ['price']
    list_filter = ['prod_date']
    search_fields = ['description']
    search_help_text = 'Search by Description field'
    fields = ['product_name', 'description', 'price', 'amount', 'prod_date']
    readonly_fields = ['prod_date', 'amount']


admin.site.register(Author, AuthorAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Buyer, BuyerAdmin)
admin.site.register(Products, ProductsAdmin)
admin.site.register(Orders, OrdersAdmin)
admin.site.register(GameModel)
