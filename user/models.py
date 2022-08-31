from pyexpat import model
from django.db import models
from django.contrib.auth.models import User
import uuid
# Create your models here.

class UserModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.FloatField(default=0)
    phone = models.CharField(max_length=25)
