from django import forms
from django.core.exceptions import ValidationError
from django.core import validators
from django.forms import ModelForm
from barkasse.models import Transaction

# Create the form class.
class TransactionForm(ModelForm):
    class Meta:
        model = Transaction
        # fields = ['name', 'breed', 'comments']
        fields = '__all__'


# References

# https://docs.djangoproject.com/en/3.0/ref/forms/api/
# https://docs.djangoproject.com/en/3.0/ref/forms/fields/#datefield
# https://docs.djangoproject.com/en/3.0/ref/forms/validation/#using-validation-in-practice
# https://docs.djangoproject.com/en/3.0/ref/validators/
