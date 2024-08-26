from collections import defaultdict

def agrupar_productos(productos):
    agrupados = defaultdict(lambda: defaultdict(lambda: defaultdict(list)))
    
    for i, producto in enumerate(productos, start=1):
        fabricante = producto['Fabricante']
        categoria = producto['Categoría']
        genero = producto['Género']
        
        agrupados[fabricante][categoria][genero].append(f"Producto {i}")
    

    return convertir_a_dict(agrupados)

def convertir_a_dict(d):
    if isinstance(d, defaultdict):
        d = {k: convertir_a_dict(v) for k, v in d.items()}
    return d


productos = [
    {'Nombre': 'Zapatos XYZ', 'Código de barras': '8569741233658', 'Fabricante': 'Deportes XYZ', 'Categoría': 'Zapatos', 'Género': 'Masculino'},
    {'Nombre': 'Zapatos ABC', 'Código de barras': '7452136985471', 'Fabricante': 'Deportes XYZ', 'Categoría': 'Zapatos', 'Género': 'Femenino'},
    {'Nombre': 'Camisa DEF', 'Código de barras': '5236412896324', 'Fabricante': 'Deportes XYZ', 'Categoría': 'Camisas', 'Género': 'Masculino'},
    {'Nombre': 'Bolso KLM', 'Código de barras': '5863219635478', 'Fabricante': 'Carteras Hi-Fashion', 'Categoría': 'Bolsos', 'Género': 'Femenino'}
]

resultado = agrupar_productos(productos)
print(resultado)
