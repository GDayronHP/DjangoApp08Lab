import requests
from django.shortcuts import render, redirect

#Endpoint
BASE_URL = 'https://api-inventario-wuth.onrender.com/api/inventario/'

def lista_productos(request):


    response = requests.get(BASE_URL)
    
    if response.status_code == 200:
        datos = response.json()
    else:
        datos = []

    # Filtrado por búsqueda (por nombre)
    query = request.GET.get('q')
    if query:
        datos = [d for d in datos if query.lower() in d['nombre'].lower()]

    # Ordenamiento por campo
    ordenar_por = request.GET.get('ordenar_por')
    if ordenar_por:
        datos = sorted(datos, key=lambda x: x.get(ordenar_por, ''))

    return render(request, 'productos.html', {'datos': datos})

def crear_producto(request):
    if request.method == 'POST':
        nuevo_producto = {
            'nombre': request.POST['nombre'],
            'precio': request.POST['precio'],
            'descripcion': request.POST['descripcion'],
            'stock': request.POST['stock'],
            'foto': request.POST['foto']
        }
        requests.post(BASE_URL, json=nuevo_producto)
        return redirect('lista_productos') 
    return render(request, 'crear_producto.html')

def editar_producto(request, id):
    if request.method == 'POST':
        producto_actualizado = {
            'nombre': request.POST['nombre'],
            'precio': request.POST['precio'],
            'descripcion': request.POST['descripcion'],
            'stock': request.POST['stock'],
            'foto': request.POST['foto']
        }
        requests.put(f'{BASE_URL}{id}/', json=producto_actualizado)
        return redirect('lista_productos')

    response = requests.get(f'{BASE_URL}{id}/')
    producto = response.json() if response.status_code == 200 else {}
    return render(request, 'editar_producto.html', {'producto': producto})

def eliminar_producto(request, id):
    requests.delete(f'{BASE_URL}{id}/')
    return redirect('lista_productos')