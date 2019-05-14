from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50, db_index=True)
    slug = models.SlugField(max_length=50, unique=True)
    body = models.TextField(blank=True, db_index=True)
    date_pub =models.DateTimeField(auto_now_add=False)

    def __str__(self):
        return '{}'.format(self.title)
    
