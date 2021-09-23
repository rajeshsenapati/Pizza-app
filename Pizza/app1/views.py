# from django.shortcuts import render
# from .models import PizaModel
# from django.http import JsonResponse

# # Create your views here.

# def pizza_list(request):
#     pizza = PizaModel.objects.all()
#     data = {
#         'pizzas'
#         : list(pizza.values())
#         }
#     return JsonResponse(data)

# def pizza_details(request, pk):
#     pizza = PizaModel.objects.get(pk=pk)
#     data = {
#         'name': pizza.name,
#         'description': pizza.description,
#         'active': pizza.active
#     }
#     return JsonResponse(data)