from django.shortcuts import render, redirect, HttpResponse
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

