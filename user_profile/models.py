from django.db import models

# Create your models here.
class Logs(models.Model):
    created_ad=models.DateTimeField(auto_now_add=True, blank=True)
    update_at=models.DateTimeField(auto_now_add=True, blank=True)
    user=models.ForeignKey('auth.User', on_delete=models.CASCADE)
    action=models.CharField(max_length=10)
    url=models.CharField(max_length=100)

class Pontaj(models.Model):
    user=models.ForeignKey('auth.User', on_delete=models.CASCADE)
    start_date=models.DateTimeField()
    end_date=models.DateTimeField(null=True)

