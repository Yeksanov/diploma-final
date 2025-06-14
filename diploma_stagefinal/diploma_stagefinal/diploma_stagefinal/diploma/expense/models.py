from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Expense(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    salary = models.IntegerField(default=0)
    name = models.CharField(max_length=100, default='something')
    income = models.IntegerField(default=0)
    expenses = models.IntegerField(default=0)
    date = models.DateField(auto_now_add=False, null=True, blank=True)
class SavingsGoal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='expense_savings_goals')
    name = models.CharField(max_length=100)
    target_amount = models.IntegerField()
    current_amount = models.IntegerField(default=0)  
    deadline = models.DateField()

    def __str__(self):
        return self.name