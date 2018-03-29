from django.shortcuts import render
from .models import Customer
from django.http import JsonResponse, Http404, HttpResponse

def getJSON(request,customer_id):
    try:
        c = Customer.objects.get(pk=customer_id)
    except Customer.DoesNotExist:
        raise Http404('Customer Does not exist')

    data_out = {
                'id': c.id,
                'name': c.name,
                'month': c.month,
                'total_charges': c.total_charges,
                'recent_pmt_amt': c.recent_pmt_amt,
                'recent_pmt_date': {
                                    'date': c.recent_pmt_date_date,
                                    'month': c.recent_pmt_date_month,
                                    'year': c.recent_pmt_date_year
                                    },
                'overall_balance': c.overall_balance,
                'min_payment': c.min_payment,
                'due_date': {
                             'date': c.due_date_date,
                             'month': c.due_date_month,
                             'year': c.due_date_year
                             },
                'points_earned_month': c.points_earned_month,
                'total_pints_earned': c.total_points_earned,
                'expense_distribution':{
                                         'food': c.expense_distribution_food,
                                         'entertainment': c.expense_distribution_entertainment,
                                         'automobile': c.expense_distribution_automobile,
                                         'healthcare': c.expense_distribution_healthcare,
                                         'merchandise': c.expense_distribution_merchandise
                                         }
            }

    return JsonResponse(data_out)

def index(request):
    return HttpResponse("Hellow world")





