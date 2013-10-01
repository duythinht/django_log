from django.db import models

# Create your models here.
class Log(models.Model):
    log_type = models.CharField(max_length=30)
    log_name = models.CharField(max_length=30)
    log_value = models.CharField(max_length=100)
    log_time = models.DateTimeField(auto_now_add=True)