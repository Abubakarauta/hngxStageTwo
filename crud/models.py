from django.db import models
from django.utils import timezone
from django.core.validators import RegexValidator

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=100, validators= [
        RegexValidator(
            regex= r'^[a-zA-Z\s]*$',
            message= 'Name should only contain letters and spaces',
            code= 'invalid_name'
        ),
    ]
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



    def __str__(self):
        return self.name