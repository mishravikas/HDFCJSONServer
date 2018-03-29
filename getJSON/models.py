from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=200)
    month = models.CharField(max_length=200)
    total_charges =  models.CharField(max_length=200)
    recent_pmt_amt = models.CharField(max_length=200)
    recent_pmt_date_date =  models.CharField(max_length=2)
    recent_pmt_date_month = models.CharField(max_length=20)
    recent_pmt_date_year =  models.CharField(max_length=4)
    overall_balance = models.CharField(max_length=200)
    min_payment = models.CharField(max_length=200)
    due_date_date = models.CharField(max_length=2)
    due_date_month = models.CharField(max_length=20)
    due_date_year = models.CharField(max_length=4)
    points_earned_month = models.CharField(max_length=200)
    total_points_earned = models.CharField(max_length=200)
    expense_distribution_food = models.CharField(max_length=200)
    expense_distribution_entertainment = models.CharField(max_length=200)
    expense_distribution_automobile =  models.CharField(max_length=200)
    expense_distribution_healthcare = models.CharField(max_length=200)
    expense_distribution_merchandise = models.CharField(max_length=200)

