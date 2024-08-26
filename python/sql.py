import sqlite3


conexion = sqlite3.connect('basedatos.db')
cursor = conexion.cursor()


consulta = """
SELECT order_id, amount_total, customer_name
FROM orden_venta
WHERE amount_total > 1000;
"""


cursor.execute(consulta)


resultados = cursor.fetchall()


for fila in resultados:
    print(fila)


conexion.close()
