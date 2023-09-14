from django import forms
from .models import Author, Post, Products


class AddAuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'surname', 'email', 'biography', 'bd']


class AddPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'post', 'author', 'category']


class UpdateProductForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = ['product_name', 'price']
