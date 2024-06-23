from bd import obtener_conexion

def insertar_vehiculo(placa, modelo, serie):
    conexion = obtener_conexion()
    try:
        with conexion.cursor() as cursor:
            cursor.execute("INSERT INTO vehiculos (placa, modelo, serie) VALUES (%s, %s, %s)", 
                           (placa, modelo, serie))
        conexion.commit()
    finally:
        conexion.close()

def obtener_vehiculos():
    conexion = obtener_conexion()
    try:
        with conexion.cursor() as cursor:
            cursor.execute("SELECT placa, modelo, serie FROM vehiculos")
            vehiculos = cursor.fetchall()
    finally:
        conexion.close()
    return vehiculos

def eliminar_vehiculo(placa):
    conexion = obtener_conexion()
    try:
        with conexion.cursor() as cursor:
            cursor.execute("DELETE FROM vehiculos WHERE placa = %s", (placa,))
        conexion.commit()
    finally:
        conexion.close()

def actualizar_vehiculo(placa, modelo, serie):
    conexion = obtener_conexion()
    try:
        with conexion.cursor() as cursor:
            cursor.execute("UPDATE vehiculos SET modelo = %s, serie = %s WHERE placa = %s", 
                           (modelo, serie, placa))
        conexion.commit()
    finally:
        conexion.close()
