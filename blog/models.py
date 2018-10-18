from django.db import models
from django.utils import timezone

class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    # blank=True means field is not required (form validation)
    # null=True  means a blank field (None in python) is translated to NULL in the database
    n_pies = models.PositiveSmallIntegerField(blank=True, null=True) # careful---0 is also allowed by this field

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
