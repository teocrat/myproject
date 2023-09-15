from django.db import models
from django.db.models import Manager
from django.urls import reverse


class GameModel(models.Model):
    result = models.CharField(max_length=10)
    played = models.DateTimeField(auto_now_add=True)

    objects = Manager()

    def __str__(self) -> str:
        return f"Результат игры: {self.result}, время: {self.played}"

    class Meta:
        ordering = ['-played']

    @staticmethod
    def return_last(n):
        return GameModel.objects.all()[:n]


class Author(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    email = models.EmailField()
    biography = models.TextField()
    bd = models.DateField()

    def get_absolute_url(self):
        return reverse('author_page', kwargs={'pk': self.pk})

    def __str__(self):
        return f'{self.name} {self.surname}'


class Post(models.Model):
    title = models.CharField(max_length=200)
    post = models.TextField()
    date = models.DateField(auto_now_add=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.CharField(max_length=100)
    viewed = models.IntegerField(default=0)
    published = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse('detail_post', kwargs={'pk': self.pk})

    def __str__(self):
        return f'{self.author} - {self.title} - {self.published} - {self.date}'


class Buyer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=100)
    address = models.CharField(max_length=500)
    reg_data = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'Name: {self.name} - Email: {self.email}'


class Products(models.Model):
    product_name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    amount = models.IntegerField()
    prod_date = models.DateField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('prod_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return f'Product: {self.product_name} - Price: {self.price} - Amount: {self.amount}'


class Orders(models.Model):
    client = models.ForeignKey(Buyer, on_delete=models.CASCADE)
    product = models.ManyToManyField(Products)
    sum_order = models.DecimalField(max_digits=10, decimal_places=2)
    order_date = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['-id']

    @staticmethod
    def return_last(n):
        return Orders.objects.all()[:n]

    def __str__(self):
        return f'Buyer: {self.client} - Product: {self.product} - Sum: {self.sum_order}'
