def calcular_descuento(total_venta):
    """
    Calcula el porcentaje de descuento a aplicar basado en el total de la venta.
    
    Parámetros:
    total_venta (float): El total de la venta en dólares.

    Retorna:
    float: El porcentaje de descuento aplicable.
    """
    if total_venta > 500:
        return 10  
    elif 100 <= total_venta <= 500:
        return 5   
    else:
        return 0   


try:
    total_venta = float(input("Ingrese el total de la venta: "))
    descuento = calcular_descuento(total_venta)
    print(f"El porcentaje de descuento aplicable es: {descuento}%")
except ValueError:
    print("Error: Por favor ingrese un número válido.")
