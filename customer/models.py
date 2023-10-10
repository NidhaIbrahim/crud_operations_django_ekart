from django.db import models

# Create your models here.

class Customer(models.Model):
    first_name = models.CharField( max_length = 30 )
    last_name = models.CharField( max_length = 30 )
    email = models.CharField( max_length = 50 )
    gender = models.CharField( max_length = 10 )
    city = models.CharField( max_length = 30 )
    country = models.CharField( max_length = 30 )
    password = models.CharField( max_length = 20 )

    class Meta:
        db_table = 'customer_tbl'

