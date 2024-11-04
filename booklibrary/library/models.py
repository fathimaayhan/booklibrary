from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=100,null=True)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=100,null=True)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    author = models.ForeignKey(Author,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/',blank=True,null=True)

    




    def __str__(self):
        return self.title
    

