from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.


# création du mouchard
class Security(models.Model):
    created_by = models.CharField(max_length=50, null=True, blank=True)
    modified_by = models.CharField(max_length=50, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    # on ne supprime rien dans la BD
    is_deleted = models.BooleanField(default=False)

    class Meta:
        abstract = True

    def save(self, author="system", *args, **kwargs):
        try:
            self.objects.get(pk=self.pk)
        except Exception:
            self.created_by = author
        self.modified_by = author
        super().save(*args, **kwargs)

    def delete_as(self, author):
        self.is_deleted = True
        self.save(author)


class Store(Security):
    # pas besoin d'ecrire l'ID Django génère ca automatiquement
    name = models.CharField(max_length=50)
    description = models.TextField(null=True)
    #phone = models.CharField(max_length=50)
    #logo =  models.FileField(null=True)


class Person(models.Model):
    user = models.OneToOneField(User, models.CASCADE)
    # pp = models.FileField(null=True)
    # c'est plus s tôt models.Imagefield(upload_to='un dossier')
    #on doit installer pillow avant

    #une personne appartient à une boutique
    store = models.ForeignKey(Store, models.PROTECT)


class Customer(Security):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=50)
    person = models.ManyToManyField(Person, through='Message')
    #un client pour une boutique
    store = models.ForeignKey(Store, models.PROTECT)


class Message(Security):
    person = models.ForeignKey(Person, on_delete=models.PROTECT)
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)
    object = models.CharField(max_length=50)
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)


class Category(Security):
    name = models.CharField(max_length=50)
    store = models.ForeignKey(Store, models.PROTECT)


class Product(Security):
    designation = models.CharField(max_length=50)
    date_ent_stock = models.DateTimeField(default=timezone.now)
    date_peremption = models.DateTimeField(default=timezone.now)
    # Qtté_entree
    stock_init = models.PositiveIntegerField()
    # stock
    stock_dt = models.PositiveIntegerField()
    price_ini = models.FloatField()
    price_promo = models.FloatField(null=True)
    store = models.ForeignKey(Store, models.PROTECT)
    category = models.ForeignKey(Category, models.PROTECT)
