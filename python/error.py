mi_diccionario = {'a': 1, 'b': 2, 'c': 3}

try:
    valor = mi_diccionario['d']
except KeyError:
    print("La clave no existe en el diccionario.")
    valor = None  

print(valor)

# try-except: Es útil cuando se desea manejar explícitamente el error y realizar una acción específica si la clave no existe. Es una forma robusta de prevenir que el programa se detenga debido a un error inesperado





mi_diccionario = {'a': 1, 'b': 2, 'c': 3}

valor = mi_diccionario.get('d', "Clave no encontrada")

print(valor)

# get(): Es una forma común de acceder a claves en un diccionario cuando existe la posibilidad de que la clave no esté presente. Este método devuelve un valor predeterminado en lugar de lanzar una excepción.