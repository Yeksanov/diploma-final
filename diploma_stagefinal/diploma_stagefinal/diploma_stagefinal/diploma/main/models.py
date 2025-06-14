from django.db import models
from django.contrib.auth.models import User

class Expense(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='expenses')
    salary = models.IntegerField(default=0)
    name = models.CharField(max_length=100, default='something')
    income = models.IntegerField(default=0)
    expenses = models.IntegerField(default=0)
    date = models.DateField(auto_now_add=False, null=True, blank=True)


class SavingsGoal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    target_amount = models.IntegerField()
    current_amount = models.IntegerField(null=True, blank=True)
    deadline = models.DateField()

    def __str__(self):
        return self.name

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name} ({self.email})"