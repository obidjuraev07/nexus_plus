from django.db import models
from django.template.defaultfilters import slugify
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

def default_location():
    return {
        "region": "",
        "district": ""
    }
class Category(models.Model):
    name = models.CharField(max_length=50,  null=False, blank=False)
    parent = models.ForeignKey('self', related_name='father', on_delete=models.CASCADE, blank=True, null=True)
    slug = models.SlugField()

    def save(self, *args, **kwargs):
        if self.parent and self.parent.name == self.name:
            raise ValidationError('Xato....')
        else:
            if not self.slug:
                self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.name}'


class Image(models.Model):
    image = models.ImageField(upload_to='static/img/')


class Product(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.IntegerField()
    decription = RichTextField()
    phone_number = models.CharField(max_length=13)
    location = models.JSONField(default=default_location, blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)


class ProductImage(models.Model):
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)