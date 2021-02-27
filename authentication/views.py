from django.shortcuts import render, redirect
from django.views import View
from django.http import JsonResponse
from django.contrib.auth.models import User
import json
from validate_email import validate_email
from django.contrib import messages
from django.contrib import auth


# Create your views here.


class EmailValidationView(View):
    def post(self, request):
        data = json.loads(request.body)
        email = data['email']

        if not validate_email(email):
            return JsonResponse({'email_error': 'invalid email'}, status=400)
        if User.objects.filter(email=email).exists():
            return JsonResponse({'email_error': 'this email is already registered'}, status=419)

        return JsonResponse({'email_valid': True})


class UsernameValidationView(View):
    def post(self, request):
        data = json.loads(request.body)
        username = data['username']

        if not str(username).isalnum():
            return JsonResponse({'username_error': 'username should only contain alphanumeric characters'}, status=400)
        if User.objects.filter(username=username).exists():
            return JsonResponse({'username_error': 'username in use, choose another one'}, status=419)

        return JsonResponse({'username_valid': True})


class RegistrationView(View):
    def get(self, request):
        return render(request, 'authentication/register.html')

    def post(self, request):

        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        context = {
            'fieldValues': request.POST
        }
        if username and email and password:
            if not User.objects.filter(username=username).exists():
                if not User.objects.filter(email=email).exists():
                    if len(password) < 6:
                        messages.error(request, 'Password too short')
                        return render(request, 'authentication/register.html', context)

                    user = User.objects.create_user(username=username, email=email)
                    user.set_password(password)
                    user.save()
                    messages.success(request, 'Account successfully created')
                    return render(request, 'authentication/register.html')

            return render(request, 'authentication/register.html')
        messages.error(request, 'Fill all the Fields')
        return render(request, 'authentication/register.html', context)


class LoginView(View):
    def get(self, request):
        return render(request, 'authentication/login.html')

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']

        if username and password:
            user = auth.authenticate(username=username, password=password)

            if user:
                auth.login(request, user)
                messages.success(request, 'Welcome, '+user.username+' you are now logged in ')
                return redirect('index')

            messages.error(request, 'Invalid Credentials')
            return render(request, 'authentication/login.html')

        messages.error(request, 'Fill all the fields')
        return render(request, 'authentication/login.html')


class LogoutView(View):
    def get(self, request):
        auth.logout(request)
        messages.success(request, 'successfully logged out')
        return redirect('login')
