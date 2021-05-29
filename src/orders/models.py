from django.db import models

import datetime

status_choice = [
    ("Complete", "Complete"),
    ("Confirmed", "Confirmed"),
    ("Deleted", "Deleted"),
]


class Category(models.Model):
    name = models.CharField(max_length=255)


class Order(models.Model):
    status = models.CharField(max_length=20, choices=status_choice)
    # delivery_date = models.
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    product = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
