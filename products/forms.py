from django import forms
from .models import Product, ProductImage

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price']

class ProductImageForm(forms.ModelForm):
    image = forms.ImageField()

    class Meta:
        model = ProductImage
        fields = ['image']

def clean_image(self):
    image = self.cleaned_data['image']
    ext = image.name.split('.')[-1].lower()
    if ext not in ['jpg', 'jpeg', 'png']:
        raise forms.ValidationError('JPG, JPEG, PNG 파일만 업로드 가능합니다.')
    if image.size > 5 * 1024 * 1024:
        raise forms.ValidationError('5MB 이하의 이미지만 업로드 가능합니다.')
    return image