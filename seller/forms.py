from django import forms
from seller import models

class contactform(forms.ModelForm):
    class Meta:
        model = models.Contact_us
        fields = '__all__'

class Orderform(forms.ModelForm):
    class Meta:
        model = models.Order
        fields = ['phone', 'zip']

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if not str(phone).isdigit():
            raise forms.ValidationError("The phone number must contain only digits.")
        return phone

    def clean_zip(self):
        zip = self.cleaned_data.get('zip')
        # Add any custom validation for zip_code format if necessary
        return zip

class categoryform(forms.ModelForm):
    class Meta:
        model = models.Category
        fields = '__all__'

class subcategoryform(forms.ModelForm):
    class Meta:
        model = models.Sub_Category
        fields = '__all__'

class colorform(forms.ModelForm):
    class Meta:
        model = models.Color
        fields = '__all__'

class productform(forms.ModelForm):
    class Meta:
        model = models.Product
        fields = '__all__'


class orderitemform(forms.ModelForm):
    class Meta:
        model = models.OrderItem
        fields = '__all__'

class signupform(forms.ModelForm):
    class Meta:
        model = models.signup
        fields = '__all__'
