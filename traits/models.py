from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from pubs.models import Pub
from simple_history.models import HistoricalRecords

class Trait(models.Model):

    genus = models.CharField(max_length=128)
    species = models.CharField(max_length=128)

    isi = models.FloatField(blank=True, null=True,
            verbose_name='index of self-incompatibility',
            validators=[MinValueValidator(0), MaxValueValidator(1)])

    bs_choices = (('SI', 'Self-incompatible'), ('SC', 'Self-compatible'))
    breeding_system = models.CharField(blank=True, null=True, choices=bs_choices, max_length=2)

    pubref = models.ForeignKey(Pub, related_name='traitref', on_delete=models.PROTECT, verbose_name='Pub citekey')

    history = HistoricalRecords()
    changereason = models.TextField(blank=True, null=True)
    # This changereason field is copied into the history object in TraitAdmin().
    # It should probably excluded elsewhere (record view, csv export, etc.)

    def __str__(self):
        return(self.genus + ' ' + self.species)
