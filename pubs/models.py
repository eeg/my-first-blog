from django.db import models

class Pub(models.Model):

    citekey = models.CharField(max_length=128, unique=True)
    author = models.CharField(max_length=128, blank=True, null=True)
    # also has field traitref, created by ForeignKey within Trait

    def __str__(self):
        return(self.citekey)
