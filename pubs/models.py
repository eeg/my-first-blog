from django.db import models

class Person(models.Model):

    first_name = models.CharField(max_length=128, null=True, blank=True)
    last_name  = models.CharField(max_length=128)

    def __str__(self):
        name = ''
        if self.first_name != None:
            name += self.first_name + ' '
        name += self.last_name
        return(name)

class Pub(models.Model):

    citekey = models.CharField(max_length=128, unique=True)
    author = models.ManyToManyField(Person, related_name='author', null=True, blank=True)
    title = models.CharField(max_length=1024)
    # also has field traitref, created by ForeignKey within Trait

    def __str__(self):
        return(self.citekey)
