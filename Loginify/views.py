from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from . models import UserDetails
from django.contrib import messages
import json


# Create your views here.
@csrf_exempt
def Signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        if UserDetails.objects.filter(Email=email).exists(): 
            messages.error(request, 'This email already exists!!')
            return render(request, 'Components/Signup.html')
        try:
            user = UserDetails.objects.create(Username=username, Email=email, Password=password)  # Correct field names
            user.save()
            messages.success(request, 'Account created successfully! Please log in.')
            return redirect('login') 
        except Exception as e:
            messages.error(request, e)
            return render(request, 'Components/Signup.html')
    return render(request, 'Components/Signup.html')

        
@csrf_exempt       
def LoginUser(request):
    if request.method == 'POST':
        username = request.POST.get('username')  
        password = request.POST.get('password')
        user=UserDetails.objects.get(Username=username)
        if user.Password == password:
            data = {
                "username" : username
            }
            return render(request,'Components/home.html', data)  
        else:
            messages.error(request, 'Invalid username or password')
            return render(request, 'Components/Login.html')
    return render(request, 'Components/Login.html')


def HomeView(request):
    # user = UserDetails.objects.get()
    # username = user.username
    # print(username)
    # data = {
    #     "username": username
    # }
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
