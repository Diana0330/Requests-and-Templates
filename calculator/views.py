from django.contrib.sites import requests
from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'sandwich': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}


# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:

def recipe_omlet(request):
    template_name = 'calculator/index.html'
    servings = int(request.GET.get('servings', 1))
    recipe = DATA['omlet']
    new_data = {}
    for ingredient in recipe:
        amount = recipe[ingredient]
        new_data[ingredient] = round(amount * servings, 2)

    context = {
        'recipe': new_data,

    }
    return render(request, template_name, context)


def pasta_recipe(request):
    template_name = 'calculator/index.html'
    servings = int(request.GET.get('servings', 1))
    recipe = DATA['pasta']
    print(recipe)
    new_data = {}
    for ingredient in recipe:
        amount = recipe[ingredient]
        new_data[ingredient] = round(amount * servings, 2)
    print(new_data)
    context = {
        'recipe': new_data,

    }
    return render(request, template_name, context)


def sandwich_recipe(request):
    template_name = 'calculator/index.html'
    servings = int(request.GET.get('servings', 1))
    recipe = DATA['sandwich']
    print(recipe)
    new_data = {}
    for ingredient in recipe:
        amount = recipe[ingredient]
        new_data[ingredient] = round(amount * servings, 2)
    print(new_data)
    context = {
        'recipe': new_data,

    }
    return render(request, template_name, context)


def home_view(request):
    template_name = 'calculator/home.html'
    pages = {
        'Omlet page': reverse('omlet'),
        'Pasta page': reverse('pasta'),
        'Sandwich page': reverse('sandwich')
    }

    context = {
        'pages': pages,

    }
    return render(request, template_name, context)
