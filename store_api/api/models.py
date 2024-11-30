from django.db import models
from uuid import uuid4
from django.core.exceptions import ValidationError


def PositiveValidator(value):
    if value < 0:
        raise ValidationError('Value must be positive')
    return value


class Token(models.Model):

    token = models.CharField(max_length=36, unique=True)

    def __str__(self):
        return self.token

class Good(models.Model):
    name = models.CharField(max_length=100)
    amount = models.IntegerField(validators=[PositiveValidator])
    price = models.IntegerField(validators=[PositiveValidator])

    def __str__(self):
        return self.name

# Create your models here.
