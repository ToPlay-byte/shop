from django.db import models
from django.conf import settings
from django.utils import timezone
from apps.catalog.models import Product


class Order(models.Model):
    first_name = models.CharField(verbose_name='First name', max_length=16)
    last_name = models.CharField(verbose_name='Last name', max_length=16)
    email = models.EmailField(verbose_name='Email')
    country = models.ForeignKey('cities_light.Country', verbose_name='Country', on_delete=models.CASCADE, default=1)
    city = models.ForeignKey('cities_light.City', verbose_name='City', on_delete=models.CASCADE, default=1)
    post_code = models.PositiveIntegerField(verbose_name='Post code')
    product = models.ForeignKey(Product, verbose_name="Toy's name", on_delete=models.CASCADE)
    created = models.DateField(verbose_name='Created', default=timezone.now)
    paid = models.BooleanField(default=False)
    address = models.CharField(verbose_name='Address', max_length=50)
    active = models.BooleanField(default=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='User', null=True, on_delete=models.CASCADE)
    quantity = models.IntegerField(verbose_name='Quantity', default=1)
    total_price = models.DecimalField(verbose_name='Total price', decimal_places=2, max_digits=10, default=20.0)

    def save(
            self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        Product.objects.filter(name=self.product.name).update(quantity=models.F('quantity') - self.quantity)
        return super().save(force_insert, force_update, using, update_fields)

    def delete(self, using=None, keep_parents=False):
        Product.objects.filter(name=self.product.name).update(quantity=models.F('quantity') + self.quantity)
        return super().delete(using, keep_parents)

    def __str__(self):
        return f'{self.user}, {self.product}'





        
        
        