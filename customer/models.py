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

class Seller(models.Model):
    first_name = models.CharField( max_length = 30 )
    last_name = models.CharField( max_length = 30 )
    email = models.CharField( max_length = 50 )
    gender = models.CharField( max_length = 10 )
    city = models.CharField( max_length = 30 )
    country = models.CharField( max_length = 30 )
    seller_picture = models.ImageField( upload_to = 'seller/' )
    company_name = models.CharField( max_length = 20 )
    bank_name = models.CharField( max_length = 20 )
    bank_branch = models.CharField( max_length = 20 )
    account_number = models.CharField( max_length = 20 )
    ifsc = models.CharField( max_length = 30 )
    login_Id = models.CharField( max_length = 20 )
    password = models.CharField( max_length = 20 )
    status = models.CharField( max_length = 50, default = 'pending' )

    class Meta:
        db_table = 'seller_tbl'

