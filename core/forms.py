from django import forms
from .models import ProductReview, Product, ProductImages


class ProductReviewForm(forms.ModelForm):

    class Meta:
        model = ProductReview
        fields = ["rating", "review"]

        widgets = {
            'review': forms.Textarea(attrs={
                "placeholder": "Write a review...",
                "class": "form-control",
                "rows": 5
            }),
            'rating': forms.Select(attrs={
                'class': 'form-control'
            })
        }


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        exclude = ['vendor', 'pid', 'product_status', 'assured',
                   'featured', 'old_price', 'sku', 'date', 'updated']

        labels = {
            'warranty_period': 'Warranty period',
            'return_options': 'Return options',
            'in_stock': 'In stock',
        }

        widgets = {
            'category': forms.Select(attrs={
                'class': 'form-control',
                'placeholder': ''
            }),
            'tags': forms.TextInput(attrs={
                'class': 'form-control',
                'required': False,
                'placeholder': '',
                'title': 'comma separated names for tags'
            }),
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': ''
            }),
            'image': forms.ClearableFileInput(attrs={
                'class': 'form-control',
                'placeholder': ''
            }),
            'price': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': ''
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': '',
                "style": 'height: 300px;'
            }),
            'specifications': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': '',
                "style": 'height: 300px;'
            }),
            'manufacturer': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': ''
            }),
            'manufactured': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '',
                'required': False
            }),
            'expiring': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '',
                'required': False
            }),
            'warranty_period': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '',
                'required': False
            }),
            'size': forms.Select(attrs={
                'class': 'form-control',
                'placeholder': '',
                'required': False
            }),
            'return_options': forms.Select(attrs={
                'class': 'form-control',
                'placeholder': ''
            }),
            'stock_quantity': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': ''
            }),
        }


class ProductThumbnailImageForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ['image']

        labels = {
            'image': 'Upload an updated Image'
        }

        widgets = {
            'image': forms.ClearableFileInput(attrs={
                'class': 'form-control'
            })
        }


class UpdateProductForm(forms.ModelForm):

    class Meta:
        model = Product
        exclude = ['vendor', 'image', 'tags', 'pid', 'product_status', 'assured',
                   'featured', 'sku', 'date', 'updated']

        widgets = {
            'category': forms.Select(attrs={
                'class': 'form-control',
                'placeholder': ''
            }),
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': ''
            }),
            'price': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': ''
            }),
            'old_price': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': ''
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': '',
                "style": 'height: 300px;'
            }),
            'specifications': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': '',
                "style": 'height: 300px;'
            }),
            'manufacturer': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': ''
            }),
            'manufactured': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '',
                'required': False
            }),
            'expiring': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '',
                'required': False
            }),
            'warranty_period': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '',
                'required': False
            }),
            'size': forms.Select(attrs={
                'class': 'form-control',
                'placeholder': '',
                'required': False
            }),
            'return_options': forms.Select(attrs={
                'class': 'form-control',
                'placeholder': ''
            }),
            'stock_quantity': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': ''
            }),
        }


class ProductImagesForm(forms.ModelForm):

    class Meta:
        model = ProductImages
        fields = ['image', 'image_text']
        widgets = {
            'image': forms.ClearableFileInput(attrs={'class': 'form-control', 'placeholder': ''}),
            'image_text': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}),
        }
