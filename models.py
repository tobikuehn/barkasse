from django.db import models

class Transaction(models.Model):
    """A transaction of money"""
    title = models.CharField(max_length=100, null=True)
    amount = models.FloatField()
    shop = models.ForeignKey('Shop', on_delete=models.SET_NULL, null=True)
    account = models.ForeignKey('Account', on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """String for representing the Model object."""
        return self.title


class Shop(models.Model):
    """A shop from where we buy stuff"""
    name = models.CharField(max_length=100)

    def __str__(self):
        """String for representing the Model object."""
        return self.name

class Account(models.Model):
    """A bank account we use to pay"""
    name = models.CharField(max_length=100)
    comment = models.TextField(null=True)

    def __str__(self):
        """String for representing the Model object."""
        return self.name