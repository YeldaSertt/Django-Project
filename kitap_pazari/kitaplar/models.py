
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User

# Create your models here.
class Book(models.Model):
  name = models.CharField(max_length=255)
  author = models.CharField(max_length=255)
  desc = models.TextField(blank=True, null=True)

  date = models.DateTimeField(auto_now_add=True)
  update_date =  models.DateTimeField(auto_now=True)
  release_date = models.DateTimeField()

  def __str__(self):
      return f'{self.name} - {self.author}'




class Comment(models.Model):
  book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='comments')

  # yorum_sahibi =  models.CharField(max_length=255)
  comment_own = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_comment')
  comment = models.TextField(blank=True, null=True)

  date = models.DateTimeField(auto_now_add=True)
  update_date =  models.DateTimeField(auto_now=True)

  rate = models.PositiveIntegerField(
      validators = [MinValueValidator(1), MaxValueValidator(5)],
  )


  def __str__(self):
      return str(self.rate)

  
  
