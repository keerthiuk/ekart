from django.db import models

# Create your models here.
class EkartAdmin(models.Model):
    user_name = models.CharField(max_length=50)
    passsword = models.CharField(max_length=50)

    class Meta:
        db_table = 'admin_tb'