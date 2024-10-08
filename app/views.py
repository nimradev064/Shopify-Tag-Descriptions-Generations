from django.shortcuts import render
from django.http import JsonResponse
from .models import tagdescription

def product_list(request):
    return render(request, 'product_list.html')

def get_all_tags(request):
    tags = tagdescription.objects.all().values('title', 'image', 'tags', 'description')
    return JsonResponse(list(tags), safe=False)
