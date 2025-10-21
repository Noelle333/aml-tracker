from django.db import models

class Case(models.Model):
    STATUS_CHOICES = [
        ('open', 'Open'),
        ('review', 'Under Review'),
        ('closed', 'Closed')
    ]

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    account_number = models.CharField(max_length=50)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='open')
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
