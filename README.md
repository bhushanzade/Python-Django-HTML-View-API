# Python-Django-HTML-View-API
This is simple demo of python django rest framework without rest api we using simple html response how to display data.

To see python steps for run django rest framework follow this first 11 steps.
Link https://github.com/bhushanzade/Python-Django-Rest-API-Demo

In our basic example without using rest api we can manually display html response using django framework instead of JSON response.

to see example download this git repository and follow some step from above link

and after this add this code into views.py file


    from django.shortcuts import render
    from django.http import HttpResponse

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


after this just register this employee_html_view under the url.py file

    from django.contrib import admin
    from django.urls import path
    from myproject1.api import views

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('api/', views.employee_html_view)
    ]

and run the server using cmd py manage.py runserver

open browser to see result and add this link to opened browser i.e. http://127.0.0.1:8000/api/

Finish.

# Thank You!
