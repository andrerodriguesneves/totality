from django.db import models

class Precatory(models.Model):

    entity = models.CharField(max_length=200, db_index=True)
    protocol = models.CharField(max_length=30)
    precatory = models.CharField(max_length=200, db_index=True)
    situation = models.CharField(max_length=200, db_index=True)
    original_process = models.CharField(max_length=200, db_index=True)
    nature = models.CharField(max_length=200, db_index=True)   
    year = models.CharField(max_length=4)
    historical_value = models.DecimalField(max_digits=10, decimal_places=2)
    paid_out = models.BooleanField()    

    class Meta:
        verbose_name = "Precatory"
        verbose_name_plural = "Precatorys"

    def __str__(self):
        return self.precatory

