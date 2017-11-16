from django import forms
from .models import OrderHeader, OrderDetails

class OrderHeaderForm(forms.ModelForm):

    class Meta:
        model = OrderHeader
        fields = ('customer_name', 'customer_email', 'customer_mobile', 'order_date', 'ordered_by_date', 'description')


class OrderDetailsForm(forms.ModelForm):

    class Meta:
        model = OrderDetails
        fields = ('number_line', 'board_number', 'description')