from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
class person(models.Model):
    name = models.CharField(max_length=100, validators= [
        RegexValidator(
            regex= r'^[a-zA-Z\s]*$',
            message= 'Name should only contain letters and spaces',
            code= 'invalid_name'
        ),
    ]
    )



    def __str__(self):
        return self.name