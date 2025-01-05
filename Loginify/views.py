from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from . models import UserDetails
from django.contrib import messages
import json
from .forms import SignupForm, LoginForm


# Create your views here.
@csrf_exempt
def Signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            try:
                user = UserDetails.objects.create(Username=username,Email=email,Password=password)
                user.save()
                messages.success(request, 'Account created successfully! Please log in.')
                return redirect('login')
            except Exception as e:
                    messages.error(request, f"An error occurred: {e}")
        else:
            messages.error(request, 'Invalid form submission.')
    else:
        form = SignupForm()
    return render(request, 'Components/Signup.html', {'form': form})

        
@csrf_exempt       
def LoginUser(request):
    if request.method == 'POST':
        if request.session.get('username'):
            return JsonResponse({
                "success" : True,
                "message" : f"{request.session.get('username')} is already logged in!!"
            })
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            try :
                user = UserDetails.objects.get(Username=username)
                if user.Password == password:  
                    request.session['username'] = user.Username
                    request.session.set_expiry(10) 
                    data = {
                        "username": username
                    }
                    return render(request, 'Components/Home.html', data)
                else:
                    messages.error(request, "Invalid Password or Username!!")
            except UserDetails.DoesNotExist:
                messages.error(request, "User does not exist!!")
        else:
            messages.error(request, "Invalid Form!!")    
    else:
        form = LoginForm()
    return render(request, 'Components/Login.html', {'form' : form})


def HomeView(request):
    # user = UserDetails.objects.get()
    # username = user.username
    # print(username)
    return render(request, 'Components/home.html')


@csrf_exempt
def getUsers(request):
    users = UserDetails.objects.all().values()  
    return JsonResponse(list(users), safe=False)


@csrf_exempt
def get_by_email(request, email):
    try:
        user = UserDetails.objects.get(Email=email) 
        return JsonResponse({
            'username': user.Username,
            'email': user.Email
        })
    except UserDetails.DoesNotExist:
        return HttpResponse('User not found', status=404)
    

@csrf_exempt
def updateUser(request, email):
    try:
        user = UserDetails.objects.get(Email=email)
        if request.method == 'POST':
            data = json.loads(request.body)
            user.Username = data.get('username', user.Username)
            user.Email = data.get('email', user.Email)
            user.save()
            return JsonResponse({
                'message': 'User updated successfully',
                'username': user.Username,
                'email': user.Email
            })
        else:
            return HttpResponse('Error')
    except UserDetails.DoesNotExist:
        return HttpResponse('User not found', status=404)


@csrf_exempt
def deleteUser(request, email):
    if request.method == 'DELETE': 
        try:
            user = UserDetails.objects.get(Email=email)  
            user.delete() 
            return JsonResponse({'message': 'User deleted successfully'})
        except UserDetails.DoesNotExist:
            return HttpResponse('Cannot find user', status=404)
    return HttpResponse('Invalid', status=400)
