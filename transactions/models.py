from statistics import mode
from django.db import models
from django.contrib.auth.models import User
import django

# Create your models here.


class TrcnHistoryModel(models.Model):
    h_trcn_frm = models.OneToOneField(User, on_delete=models.CASCADE, related_name='h_trcn_frm')
    h_trcn_to = models.OneToOneField(User, on_delete=models.CASCADE)
    h_product_name = models.TextField(default='')
    h_amount = models.FloatField()
    facture_file = models.FileField(upload_to='factures/')
    h_date = models.DateTimeField(default=django.utils.timezone.now)