from django.db import models
from django.urls import reverse

# Create your models here.

class Category(models.Model):
    name = models.CharField('Nome', max_length=100, unique=True)
    slug = models.SlugField('Identificador', max_length=100, unique=True)
    
    created= models.DateTimeField('Criado em :', auto_now_add=True)
    modified = models.DateTimeField('Modificado em :', auto_now_add=True)
    

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['name']

    def __str__(self):
        return self.name


    def get_absolute_url(self):
        return reverse('categoria', kwargs={'slug': self.slug})
    

class Product(models.Model):
    name = models.CharField('Nome', max_length=100, unique=True)
    slug = models.SlugField('Identificador', max_length=100, unique=True)
    category = models.ForeignKey('Lux.Category', on_delete=models.CASCADE)
    description = models.TextField('Descrição', blank=True)
    price = models.DecimalField('Preço', decimal_places=2, max_digits=8)

    created = models.DateTimeField('Criado em', auto_now_add=True)
    modified = models.DateTimeField('Modificado em', auto_now=True)

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'
        ordering = ['name']

    
    def __str__(self):
        return self.name