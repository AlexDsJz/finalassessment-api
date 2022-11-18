from app.models import Process, User
from django.shortcuts import get_object_or_404
from domain.algorithm import get_minimum_value

def create_process(string_triangle, user_id): 
    user = get_object_or_404(User, pk = user_id)
    list = string_triangle.split(';')
    triangle = []
    try:
        for item in list:
            sublist = []
            for element in item.split(' '):
                sublist.append(int(element))
            triangle.append(sublist)
    except:
        print("Ocurrio un error")
        
    minimum_sum = get_minimum_value(triangle, 0 , 0)
    
    process = Process.objects.create(input = triangle, output = minimum_sum, user = user)
    process.save()
    
    return minimum_sum