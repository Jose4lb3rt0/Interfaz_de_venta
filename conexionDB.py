import mysql.connector

class Registro_Datos:

    def __init__(self):
        try:
            # Reemplaza 'user', 'password', 'host', y 'database' con tus propios valores
            self.conexion = mysql.connector.connect(
                user='root',
                password='admin',
                host='localhost',
                database='interfaz_de_venta'
            )

            if self.conexion.is_connected():
                print("¡Conexión exitosa!")

        except mysql.connector.Error as err:
            print(f"Tienes un error: {err}")


    def __del__(self):
        # Cierra la conexión al destruir la instancia
        if hasattr(self, 'conexion') and self.conexion.is_connected():
            self.conexion.close()


    def inserta_venta(self, codigo, nombre, fecha, monto, igv, montofinal):
        cur = self.conexion.cursor()
        sql = '''INSERT INTO venta (codigo_venta, comprador_nombre, venta_fecha, venta_monto, venta_igv, venta_montofinal)
                VALUES('{}', '{}', '{}', '{}', '{}', '{}')'''.format(codigo, nombre, fecha, float(monto), float(igv), float(montofinal))
        cur.execute(sql)
        self.conexion.commit()
        cur.close()
        
    def conteo_detalles(self, codigo):
        cursor = self.conexion.cursor()
        sql = "SELECT count(*) FROM detalle_venta WHERE codigo_venta = {}".format(codigo)
        cursor.execute(sql)
        num = cursor.fetchone()[0]
        num = int(num)
        return num
        
    def inserta_detalles(self, codigo, productoid, pro_nombre, pro_precio, pro_cantidad, pro_total):
        cur = self.conexion.cursor()
        sql = '''INSERT INTO detalle_venta (codigo_venta, producto_id, producto_nombre, producto_precio, producto_cantidad, producto_total)
                VALUES('{}', '{}', '{}', '{}', '{}', '{}')'''.format(codigo, productoid, pro_nombre, float(pro_precio), int(pro_cantidad), float(pro_total))
        cur.execute(sql)
        self.conexion.commit()
        cur.close()

    def lista_ultima_venta(self):
        cursor = self.conexion.cursor()
        sql = "SELECT * FROM venta ORDER BY codigo_venta DESC LIMIT 1"
        cursor.execute(sql)
        num = cursor.fetchone()[0]
        return num
    
    def buscar_ventas(self):
        cursor = self.conexion.cursor()
        sql = "SELECT * FROM venta"
        cursor.execute(sql)
        registro = cursor.fetchall()
        return registro

    def busca_venta(self, ventaid):
        cur = self.conexion.cursor()
        sql = "SELECT * FROM venta WHERE codigo_venta = {}".format(ventaid)
        cur.execute(sql)
        nombreX = cur.fetchall()
        cur.close()
        return nombreX
    
    def busca_detalles(self, ventaid):
        cursor = self.conexion.cursor()
        sql = "SELECT * FROM detalle_venta WHERE codigo_venta = {}".format(ventaid)
        cursor.execute(sql)
        registro = cursor.fetchall()
        return registro
    
    def ejecutar_consulta(self, consulta):
        print("Consulta SQL:", consulta)
    
    def existe_detalle(self, venta_codigo, producto_id):
        consulta = "SELECT * FROM detalle_venta WHERE codigo_venta = {} AND producto_id = {}".format(venta_codigo, producto_id)
        try:
            resultado = self.ejecutar_consulta(consulta)
            if hasattr(resultado, '__len__'):
                return len(resultado) > 0
            else:
                return False
        except Exception as e:
            print("Error al ejecutar la consulta:", str(e))
            return False
    
    def actualiza_venta(self, monto, igv, montofinal, codigo):
        cur = self.conexion.cursor()
        sql = '''UPDATE venta SET venta_monto = '{}', venta_igv = '{}', venta_montofinal = '{}' WHERE codigo_venta = '{}' '''.format(monto, igv, montofinal, codigo)
        cur.execute(sql)
        a = cur.rowcount
        self.conexion.commit()
        cur.close()
        return a
    
    def eliminar_detalle(self, codigo, producto_id):
        cur = self.conexion.cursor()
        sql = "DELETE FROM detalle_venta WHERE codigo_venta = {} AND producto_id = {}".format(codigo, producto_id)
        cur.execute(sql)
        self.conexion.commit()
        cur.close()

    
    def sumar_detalles (self, ventaid):
        cursor = self.conexion.cursor()
        sql = "SELECT SUM(producto_total) FROM detalle_venta WHERE codigo_venta = {}".format(ventaid)
        cursor.execute(sql)
        suma_monto = cursor.fetchone()[0]
        return suma_monto

    #def carga_producto(self, codigo_producto):
    #    cur = self.conexion.cursor()
    #    sql = "SELECT nombre, modelo, precio, cantidad FROM productos WHERE CODIGO = {}".format(codigo_producto)
    #    cur.execute(sql)
    #    codigoX = cur.fetchall()
    #    cur.close()
    #    return codigoX

    #def elimina_productos(self, nombre):
    #    cur = self.conexion.cursor()
    #    sql = '''DELETE FROM productos WHERE NOMBRE = {}'''.format(nombre)
    #    cur.execute(sql)
    #    a = cur.rowcount
    #    self.conexion.commit()
    #    return a
