

from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()




    
class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, max_length=200,default='')
    content = models.TextField()
    author = models.CharField(max_length=100,default='unknown Author')
    published_date = models.DateTimeField(auto_now_add=True)
    # category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


    
    
class Sector(models.Model):
    slug = models.SlugField(unique=True, max_length=200,default='')
    name = models.CharField(max_length=100)
    articles = models.ManyToManyField(Article)
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
    
    
class Stock(models.Model):
    ticker = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=100)
    sector = models.ForeignKey(Sector, on_delete=models.CASCADE)
    revenue = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
    net_income = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
    # Add other financial metrics as needed
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.ticker)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.ticker
    
    
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name='profile')
    slug = models.SlugField(unique=True, max_length=200,default='')

    favorite_stocks = models.ManyToManyField(Stock)
    # Add other profile fields if needed
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.user.username)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.user.username
        


