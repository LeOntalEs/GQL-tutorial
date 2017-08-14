from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(blank=True, max_length=100)
    def __str__(self):
        return "{}".format(self.name)

class Document(models.Model):
    title = models.CharField(blank=True, max_length=100)
    category = models.ForeignKey(Category)
    def __str__(self):
        return "{}".format(self.title)

class Borrow(models.Model):
    borrower = models.ForeignKey(User)
    doc = models.ForeignKey(Document)
    borrow_time = models.DateTimeField(auto_now_add=True)
    return_time = models.DateTimeField(blank=True, null=True)
    def __str__(self):
        return "{}".format(self.id)
