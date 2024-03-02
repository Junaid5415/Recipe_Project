from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from .models import *


# Create your views here.


def index(request):
    if request.method == 'POST':
        data = request.POST
        
        recipe_name = data['recipe_name'] 
        recipe_desc = data['recipe_desc'] 
        recipe_image = request.FILES.get('recipe_image')

        Recipe.objects.create(
            recipe_name = recipe_name,
            recipe_desc =  recipe_desc,
            recipe_image = recipe_image,            
        )


        return redirect('index')
    
    title = 'Form'
    context = {'title': title}

    return render(request, 'index.html', context)  



def table(request):
    titles = 'Table'
    title = {'title': titles}
    queryset = Recipe.objects.all()
    return render(request, 'table.html',  {'queryset' : queryset ,**title})



def delete_recipe(request, id):
    queryset = Recipe.objects.get(id=id)
    queryset.delete()
    return redirect('table')



def edit_recipe(request, id):
    queryset = Recipe.objects.get(id=id)
    name = {'title': f'Edit_Recipe_{id}'}
    
    if request.method == 'POST':
        data = request.POST
        recipe_name = data['recipe_name']
        recipe_desc = data['recipe_desc']
        recipe_image = request.FILES.get('recipe_image')

        queryset.recipe_name = recipe_name
        queryset.recipe_desc = recipe_desc

        if recipe_image:
            queryset.recipe_image = recipe_image

        queryset.save() 
        
        return redirect('table')

    return render(request, 'update.html', {'data': queryset, **name})    



def user_register(request):

    if request.method == 'POST':
        data = request.POST

        first_name = data.get('First_Name') 
        last_name = data.get('Last_Name') 
        username = data.get('user_name')
        email = data.get('user_email', None)
        password = data.get('user_pass')

        user = User.objects.filter(username = username)
        if user.exists():
            messages.info(request, 'Username Already Exist')
            return redirect('/user_register/')
        
        user = User.objects.create(
            first_name = first_name, 
            last_name = last_name,
            username = username,
            email = email,
        )

        user.set_password(password)
        user.save()
        messages.info(request, 'Account Created Successfully! Please Login')
        return redirect('/user_login/')
    
    return render(request, 'register.html')


def user_login(request):
    user = User.objects.all()
    if request.method == 'POST':
        data = request.POST
        username = data.get('user_name')
        email = data.get('user_email')
        
    return render(request, 'login.html')

def user_logout(request):
    pass 