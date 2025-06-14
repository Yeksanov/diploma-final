from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.generic import CreateView
from .models import Expense, SavingsGoal
from .forms import DeleteGoalForm, SavingsGoalForm
from datetime import datetime
from django.db.models import Sum
from user import models
from user import forms
@login_required(login_url='/login/')
def expenses(request):
    if request.method == 'POST':
        data = request.POST
        salary = int(data.get('salary', 0))
        user = request.user
        income = int(data.get('income', 0))
        expense_amount = int(
            data.get('expense', 0)) 
        date_str = data.get('date')
        if date_str:
            date = datetime.strptime(date_str, '%Y-%m-%d').date()
        else:
            date = datetime.now().date()

       
        expense = Expense.objects.create(user=user, income=income, expenses=expense_amount, date=date)

        return redirect('expenses')

    expenses_list = Expense.objects.filter(user=request.user)
    if request.GET.get('search'):
        expenses_list = expenses_list.filter(name__icontains=request.GET.get('search'))

    total_sum = sum(expense.income for expense in expenses_list)
    total_expenses = sum(expense.expenses for expense in expenses_list)

    context = {'expenses': expenses_list, 'total_sum': total_sum, 'total_expenses': total_expenses}
    return render(request, 'expense/expenses.html', context)


@login_required(login_url='/login/')
def update_expense(request, id):
    expense = get_object_or_404(Expense, id=id)

    if request.method == 'POST':
        data = request.POST
        name = data['name']
        income = int(data.get('income', expense.income))
        expenses = int(data.get('expenses', expense.expenses))
        date_str = data.get('date')
        if date_str:
            date = datetime.strptime(date_str, '%Y-%m-%d').date()
        else:
            date = datetime.now().date()
        update_expense_data(expense, name, income, expenses, date)
        return redirect('expenses')

    context = {'expense': expense}
    return render(request, 'expense/update_expense.html', context)


@login_required(login_url='/login/')
def delete_expense(request, id):
    expense = get_object_or_404(Expense, id=id)
    expense.delete()
    return redirect('expenses')


def custom_logout(request):
    logout(request)
    return redirect('login')


@login_required(login_url='/login/')
def pdf(request):
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')
    queryset = Expense.objects.all()
    if start_date and end_date:
        start_date = datetime.strptime(start_date, '%Y-%m-%d').date()
        end_date = datetime.strptime(end_date, '%Y-%m-%d').date()
        queryset = queryset.filter(date__gte=start_date, date__lte=end_date)
    for expense in queryset:
        expense.total = expense.income - expense.expenses

    total_income = queryset.aggregate(total_income=Sum('income'))['total_income'] or 0
    total_expenses = queryset.aggregate(total_expenses=Sum('expenses'))['total_expenses'] or 0
    remaining_finance = total_income - total_expenses
    username = request.user.username

    context = {
        'expenses': queryset,
        'total_sum': total_income,
        'total_expenses': total_expenses,
        'remaining_finance': remaining_finance,
        'username': username,
        'start_date': start_date,
        'end_date': end_date
    }

    return render(request, 'expense/pdf.html', context)


def create_expense(salary, name, income, expense, date):
    Expense.objects.create(salary=salary, name=name, income=income, expenses=expense, date=date)


def update_expense_data(expense, name, income, expense_value, date):
    expense.name = name
    expense.income = income
    expense.expenses = expense_value
    expense.date = date
    expense.save()


@login_required(login_url='/login/')
def financial_statistics(request):
    expenses = Expense.objects.all()
    total_income = sum(expense.income for expense in expenses)
    total_expenses = sum(expense.expenses for expense in expenses)
    remaining_finance = total_income - total_expenses
    if total_income > 0:
        remaining_percentage = (remaining_finance / total_income) * 100
    else:
        remaining_percentage = 0

    context = {
        'total_income': total_income,
        'total_expenses': total_expenses,
        'remaining_finance': remaining_finance,
        'remaining_percentage': remaining_percentage,
    }

    return render(request, 'expense/financial_statistics.html', context)


def diagrams(request):
    expenses = Expense.objects.all()
    date_data = {}
    for expense in expenses:
        date_key = expense.date.strftime('%Y-%m-%d')
        if date_key not in date_data:
            date_data[date_key] = {'income': 0, 'expenses': 0}
        date_data[date_key]['income'] += expense.income
        date_data[date_key]['expenses'] += expense.expenses

    chart_labels = []
    chart_income = []
    chart_expenses = []
    for date, data in date_data.items():
        chart_labels.append(date)
        chart_income.append(data['income'])
        chart_expenses.append(data['expenses'])

    context = {
        'chart_labels': chart_labels,
        'chart_income': chart_income,
        'chart_expenses': chart_expenses
    }

    return render(request, 'expense/diagrams.html', context)


@login_required(login_url='/login/')
def goals(request):
    if request.method == 'POST':
        form = SavingsGoalForm(request.POST)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            return redirect('goals')
    else:
        form = SavingsGoalForm()
    
    savings_goals = SavingsGoal.objects.filter(user=request.user)
    
    delete_goal_form = DeleteGoalForm()
    if 'delete_goal' in request.POST:
        goal_id = request.POST.get('delete_goal')
        goal = get_object_or_404(SavingsGoal, id=goal_id)
        goal.delete()
        return redirect('goals')

    return render(request, 'expense/goals.html', {'form': form, 'savings_goals': savings_goals, 'delete_goal_form': delete_goal_form})


def delete_goal(request, goal_id):
    goal = get_object_or_404(SavingsGoal, id=goal_id)
    if request.method == 'POST':
        goal.delete()
        return redirect('goals')
    return redirect('goals')
def home(request):
    return render(request, 'expense/home.html')