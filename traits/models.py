from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Publocal(models.Model):

    citekey = models.CharField(max_length=128, unique=True)
    author = models.CharField(max_length=128, blank=True, null=True)
    # also has field traitref, created by ForeignKey within Trait

    def __str__(self):
        return(self.citekey)

class Trait(models.Model):

    genus = models.CharField(max_length=128)
    species = models.CharField(max_length=128)

    isi = models.FloatField(blank=True, null=True,
            verbose_name='index of self-incompatibility',
            validators=[MinValueValidator(0), MaxValueValidator(1)])

    bs_choices = (('SI', 'Self-incompatible'), ('SC', 'Self-compatible'))
    breeding_system = models.CharField(blank=True, null=True, choices=bs_choices, max_length=2)

    pubref = models.ForeignKey(Publocal, related_name='traitref', on_delete=models.PROTECT, verbose_name='Pub citekey')

    def __str__(self):
        return(self.genus + ' ' + self.species)
