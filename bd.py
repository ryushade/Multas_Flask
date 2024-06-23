import pymysql

def obtener_conexion():
    return pymysql.connect(host='semultasperu.mysql.pythonanywhere-services.com',
                                user='semultasperu',
                                password='23bf1a0d2',
                                db='semultasperu$multas')