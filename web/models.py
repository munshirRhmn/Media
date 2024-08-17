from django.db import models
from django.utils.text import slugify
from django.urls import reverse_lazy

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=20)
    slug = models.SlugField(unique=True, blank=True, null=True)
    email = models.EmailField()
    password = models.CharField(max_length=128)

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.username)  # Generate slug from username if empty
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse_lazy('web:result_show', kwargs={'slug': self.slug})

    def __str__(self):
        return self.username
    