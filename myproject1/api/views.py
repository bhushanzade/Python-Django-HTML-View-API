from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def employee_html_view(request):
    employee_table={
        'emp-no':387001,
        'emp-name':'Bhushan Zade',
        'emp-salary': 45000,
        'emp-address': 'Nashik'
    }

    response = '<h1>This is HTML response of Python Django Rest Framework </h1><h2>Employee ID : {} <br><br> Employee Name : {} <br><br> Employee Salary : {} <br><br> Employee Address : {} <br></h2>'.format(
        employee_table['emp-no'],
        employee_table['emp-name'],
        employee_table['emp-salary'],
        employee_table['emp-address'],
    )

    return HttpResponse(response)


