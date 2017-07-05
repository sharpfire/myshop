from django import forms

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]

class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(
                choices=PRODUCT_QUANTITY_CHOICES,
                coerce=int)
                # coerce=int 的 TypeChoiceField 字段来把输入转换为整数
    update = forms.BooleanField(required=False,
                initial=False,
                widget=forms.HiddenInput)