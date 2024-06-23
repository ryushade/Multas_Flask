from bd import obtener_conexion

def insertar_multa(codigo, descripcion, gravedad, precio, medida_preventiva):
    conexion = obtener_conexion()
    try:
        with conexion.cursor() as cursor:
            cursor.execute("INSERT INTO multas (codigo, descripcion, gravedad, precio, medida_preventiva) VALUES (%s, %s, %s, %s, %s)",
                           (codigo, descripcion, gravedad, precio, medida_preventiva))
        conexion.commit()
    finally:
        conexion.close()

def obtener_multas():
    conexion = obtener_conexion()
    try:
        with conexion.cursor() as cursor:
            cursor.execute("SELECT codigo, descripcion, gravedad, precio, medida_preventiva FROM multas")
            multas = cursor.fetchall()
    finally:
        conexion.close()
    return multas

def obtener_multa_por_codigo(codigo):
    conexion = obtener_conexion()
    try:
        with conexion.cursor() as cursor:
            cursor.execute("SELECT codigo, descripcion, gravedad, precio, medida_preventiva FROM multas WHERE codigo = %s", (codigo,))
            multa = cursor.fetchone()
    finally:
        conexion.close()
    return multa

def actualizar_multa(codigo, descripcion, gravedad, precio, medida_preventiva):
    conexion = obtener_conexion()
    try:
        with conexion.cursor() as cursor:
            cursor.execute("UPDATE multas SET descripcion = %s, gravedad = %s, precio = %s, medida_preventiva = %s WHERE codigo = %s",
                           (descripcion, gravedad, precio, medida_preventiva, codigo))
        conexion.commit()
    finally:
        conexion.close()

def eliminar_multa(codigo):
    conexion = obtener_conexion()
    try:
        with conexion.cursor() as cursor:
            cursor.execute("DELETE FROM multas WHERE codigo = %s", (codigo,))
        conexion.commit()
    finally:
        conexion.close()
