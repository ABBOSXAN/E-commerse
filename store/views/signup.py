from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from store.models.customer import Customer
from django.views import View


class Signup(View):
    def get(self, request):
        return render(request, 'signup.html')

    def post(self, request):
        postData = request.POST
        first_name = postData.get('firstname')
        last_name = postData.get('lastname')
        phone = postData.get('phone')
        email = postData.get('email')
        password = postData.get('password')
        value = {
            'first_name': first_name,
            'last_name': last_name,
            'phone': phone,
            'email': email
        }
        error_message = None
        customer = Customer(
            first_name=first_name,
            last_name=last_name,
            phone=phone,
            email=email,
            password=password
        )
        error_message = self.validateCustomer(customer)

        if not error_message:
            print(first_name, last_name, phone, email, password)
            customer.password = make_password(customer.password)
            customer.register()
            return redirect("homepage")
        else:
            data = {
                'error': error_message,
                'values': value
            }
            return render(request, 'signup.html', data)

    def validateCustomer(self, customer):
        error_message = None
        if not customer.first_name:
            error_message = 'Please enter your first name!!'
        elif len(customer.first_name) < 3:
            error_message = 'First name must be 3 char long or more'
        elif not customer.last_name:
            error_message = 'Please enter your last name'
        elif len(customer.last_name) < 3:
            error_message = 'Last name must be 3 char long or more'
        elif not customer.phone:
            error_message = 'Enter your phone number'
        elif len(customer.phone) < 10:
            error_message = 'Phone number must be 10 char long or more'
        elif len(customer.password) < 5:
            error_message = 'Password must be 5 char long or more'
        elif len(customer.email) < 5:
            error_message = 'Email must be 5 char long'
        elif customer.isExists():
            error_message = 'Email address already registered'

        return error_message
