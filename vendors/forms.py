from django import forms
from .models import vendor_review, vendorAddress, vendorBankDetails, Vendor, changeRequest


class vendorLoginForm(forms.Form):

    vendor_id = forms.CharField(
        max_length=20,
        label='Vendor ID',
        widget=forms.TextInput(attrs={
            'class': 'form-control'
        }))
    email = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(attrs={
            'class': 'form-control'
        }))


class VendorForm(forms.ModelForm):

    class Meta:
        model = Vendor
        fields = ['title', 'image', 'description']
        labels = {
            'title': 'Company Name',
            'image': 'Company Logo',
            'description': 'Describe Your Business'
        }
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'image': forms.ClearableFileInput(attrs={
                'class': 'form-control'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'style': 'height: 350px;'
            })
        }


class vendorbankdetailsForm(forms.ModelForm):

    class Meta:
        model = vendorBankDetails
        exclude = ['vendor']

        labels = {
            'ifsc': 'IFSC Code',
            'gst_number': 'GST Number',
            'pan_number': 'PAN Number',
            'cin': 'Company Incorporation Number'
        }

        widgets = {
            'bank_name': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'account_holder_name': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'account_number': forms.NumberInput(attrs={
                'class': 'form-control',
            }),
            'account_type': forms.Select(attrs={
                'class': 'form-control',
            }),
            'ifsc': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'branch_address': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'pan_number': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'gst_number': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'cin': forms.TextInput(attrs={
                'class': 'form-control',
            }),
        }


class vendorAddressForm(forms.ModelForm):

    class Meta:
        model = vendorAddress
        exclude = ['vendor']

        labels = {
            'status': 'Default'
        }

        widgets = {
            'floornumber': forms.TextInput(attrs={
                "class": "form-control mt-3",
            }),
            'building': forms.TextInput(attrs={
                "class": "form-control mt-3",
            }),
            'street': forms.TextInput(attrs={
                "class": "form-control mt-3",
            }),
            'city': forms.TextInput(attrs={
                "class": "form-control mt-3",
            }),
            'district': forms.TextInput(attrs={
                "class": "form-control mt-3",
            }),
            'city': forms.TextInput(attrs={
                "class": "form-control mt-3",
            }),
            'state': forms.TextInput(attrs={
                "class": "form-control mt-3",
            }),
            'country': forms.TextInput(attrs={
                "class": "form-control mt-3",
            }),
            'zipcode': forms.TextInput(attrs={
                "class": "form-control mt-3",
            }),
        }


class vendorreviewForm(forms.ModelForm):
    class Meta:
        model = vendor_review
        fields = ['review', 'rating']

        widgets = {
            'review': forms.Textarea(
                attrs={
                    "placeholder": "Write a review...",
                    "class": "form-control",
                    "style": 'height: 100px;'
                }),
            'rating': forms.Select(attrs={
                'class': 'form-control'
            })
        }


class changeRequestForm(forms.ModelForm):
    class Meta:
        model = changeRequest
        fields = ['change_field', 'reason']

        widgets = {
            'change_field': forms.Select(attrs={
                'class': 'form-control'
            }),
            'reason': forms.Textarea(attrs={
                'class': 'form-control',
                'style': 'height: 100px'
            }),
        }
