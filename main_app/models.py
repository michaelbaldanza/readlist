from django.db import models
from django.urls import reverse

class Book(models.Model):
  title = models.CharField(max_length=100)
  author = models.CharField(max_length=100, null=True, blank=True)
  genre = models.CharField(max_length=100, null=True, blank=True)
  summary = models.CharField(max_length=100, null=True, blank=True)
  pub_year = models.IntegerField(null=True, blank=True)

  def __str__(self):
    return self.name
  
  def get_absolute_url(self):
    return reverse('detail', kwargs={'book_id': self.id})