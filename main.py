import sys
from PyQt5 import uic, QtWidgets
from GUI import *
from DET import *
from conexionDB import *
from PyQt5.QtWidgets import QTableWidgetItem, QMessageBox

from DET import Ui_FormDetalles

qtCreatorFile = "detalles.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MiApp(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.datosTotal = Registro_Datos()

        self.ui.btn_cargar.clicked.connect(self.m_ventas)
        self.ui.btn_ven.clicked.connect(self.insert_venta)
        self.ui.btn_ven.clicked.connect(self.abrir)
        self.ui.btn_ven.clicked.connect(self.listar_detalles)
        self.ui.btn_buscar.clicked.connect(self.buscar_venta)
        self.ui.btn_buscar.clicked.connect(self.buscar_detalles)

        self.ui.tbl_lista.setColumnWidth(0, 98)
        self.ui.tbl_lista.setColumnWidth(1, 100)
        self.ui.tbl_lista.setColumnWidth(2, 98)
        self.ui.tbl_lista.setColumnWidth(3, 98)
        self.ui.tbl_lista.setColumnWidth(4, 98)
        self.ui.tbl_lista.setColumnWidth(5, 98)

        self.ui.tbl_venta.setColumnWidth(0, 98)
        self.ui.tbl_venta.setColumnWidth(1, 100)
        self.ui.tbl_venta.setColumnWidth(2, 98)
        self.ui.tbl_venta.setColumnWidth(3, 98)
        self.ui.tbl_venta.setColumnWidth(4, 98)
        self.ui.tbl_venta.setColumnWidth(5, 98)

    def m_ventas(self):
        datos = self.datosTotal.buscar_ventas()
        i = len(datos)

        self.ui.tbl_lista.setRowCount(i)
        tablerow = 0
        for row in datos:
            self.ui.tbl_lista.setItem(tablerow, 0, QTableWidgetItem(str(int(row[0]))))
            self.ui.tbl_lista.setItem(tablerow, 1, QTableWidgetItem(row[1]))
            self.ui.tbl_lista.setItem(tablerow, 2, QTableWidgetItem(row[2]))
            self.ui.tbl_lista.setItem(tablerow, 3, QTableWidgetItem(str(float(row[3]))))
            self.ui.tbl_lista.setItem(tablerow, 4, QTableWidgetItem(str(float(row[4]))))
            self.ui.tbl_lista.setItem(tablerow, 5, QTableWidgetItem(str(float(row[5]))))
            tablerow += 1
    
    def abrir_ventana_detalles(self):
        
        print("Botón clicado. Abriendo ventana de detalles.")
        detalles_form = QtWidgets.QWidget()
        ui_detalles_form = Ui_FormDetalles()
        ui_detalles_form.setupUi(detalles_form)
        print("Formulario abierto correctamente")
        detalles_form.show()
        
    def abrir(self):
        self.ventana=QtWidgets.QMainWindow()
        self.ud=Ui_FormDetalles()
        self.ud.setupUi(self.ventana)
        self.ventana.show()
        
        self.ud.btn_det.clicked.connect(self.insert_detalles)
        self.ud.btn_det.clicked.connect(self.listar_detalles)
        
        self.ud.btn_eli.clicked.connect(self.eli_detalles)
        self.ud.btn_eli.clicked.connect(self.listar_detalles)
        
        self.ud.tbl_detalles1.setColumnWidth(0, 98)
        self.ud.tbl_detalles1.setColumnWidth(1, 100)
        self.ud.tbl_detalles1.setColumnWidth(2, 98)
        self.ud.tbl_detalles1.setColumnWidth(3, 98)
        self.ud.tbl_detalles1.setColumnWidth(4, 98)
        self.ud.tbl_detalles1.setColumnWidth(5, 98)
    
    def insert_venta(self):
        if(self.ui.line_nom.text()=="" or self.ui.line_fec==""):
            mensaje = QMessageBox()

            mensaje.setIcon(QMessageBox.Information)

            mensaje.setWindowTitle('Mensaje Informativo')
            mensaje.setText('Ingrese los datos en las lineas de texto')

            mensaje.addButton(QMessageBox.Ok)

            respuesta = mensaje.exec_()

            if respuesta == QMessageBox.Ok:
                print('Botón OK presionado.')
        else:
            comprador_nombre = self.ui.line_nom.text()
            fecha = self.ui.line_fec.text()

            self.datosTotal.inserta_venta(0, comprador_nombre, fecha, 0, 0, 0)
            self.ui.line_nom.clear()
            self.ui.line_fec.clear()
        
    def insert_detalles(self):
        if(self.ud.line_id.text()=="" or self.ud.line_pro=="" or self.ud.line_pre=="" or self.ud.line_can==""):
            mensaje = QMessageBox()

            mensaje.setIcon(QMessageBox.Information)

            mensaje.setWindowTitle('Mensaje Informativo')
            mensaje.setText('Ingrese los datos en las lineas de texto')

            mensaje.addButton(QMessageBox.Ok)

            respuesta = mensaje.exec_()

            if respuesta == QMessageBox.Ok:
                print('Botón OK presionado.')
        else:    
            venta_id = self.datosTotal.lista_ultima_venta()
            venta_id = int(venta_id)
            producto_id = self.ud.line_id.text()
            producto_id = int(producto_id)
              
            if(self.datosTotal.conteo_detalles(venta_id)<10):
                producto_id = self.ud.line_id.text()
                producto_nombre = self.ud.line_pro.text()
                    
                producto_precio = self.ud.line_pre.text()
                producto_precio = float(producto_precio)
                    
                producto_cantidad = self.ud.line_can.text()
                producto_cantidad = int(producto_cantidad)
                try:
                    if not self.datosTotal.existe_detalle(venta_id, producto_id):
                        producto_total=producto_precio*producto_cantidad
                        producto_total=float(producto_total)

                        self.datosTotal.inserta_detalles(venta_id, producto_id, producto_nombre, producto_precio, producto_cantidad, producto_total)
                        venta_monto=self.datosTotal.sumar_detalles(venta_id)
                        venta_monto = float(venta_monto)
                        venta_igv=venta_monto*0.18
                        venta_igv = float(venta_igv)
                        venta_montofinal=venta_monto+venta_igv
                        venta_montofinal=float(venta_montofinal)
                        self.datosTotal.actualiza_venta(venta_monto,venta_igv,venta_montofinal,venta_id)
                        self.ud.line_id.clear()
                        self.ud.line_pro.clear()
                        self.ud.line_pre.clear()
                        self.ud.line_can.clear()
                except Exception as e:
                        print("Error al insertar detalles:", str(e))
                        mensaje = QMessageBox()

                        mensaje.setIcon(QMessageBox.Information)

                        mensaje.setWindowTitle('Mensaje Informativo')
                        mensaje.setText('Detalles repetidos')

                        mensaje.addButton(QMessageBox.Ok)

                        respuesta = mensaje.exec_()

                        if respuesta == QMessageBox.Ok:
                            print('Botón OK presionado.')
            else:
                mensaje = QMessageBox()

                mensaje.setIcon(QMessageBox.Information)

                mensaje.setWindowTitle('Mensaje Informativo')
                mensaje.setText('Cantidad maxima de productos alcanzada(10)')

                mensaje.addButton(QMessageBox.Ok)

                respuesta = mensaje.exec_()

                if respuesta == QMessageBox.Ok:
                    print('Botón OK presionado.')
                print("error")

    def buscar_venta(self):
        venta_id = self.ui.line_id_venta.text()
        venta_id = str("'" + venta_id + "'")

        datosB = self.datosTotal.busca_venta(venta_id)
        i = len(datosB)

        self.ui.tbl_venta.setRowCount(i)
        tablerow = 0
        for row in datosB:
            self.ui.tbl_venta.setItem(tablerow, 0, QTableWidgetItem(str(int(row[0]))))
            self.ui.tbl_venta.setItem(tablerow, 1, QTableWidgetItem(row[1]))
            self.ui.tbl_venta.setItem(tablerow, 2, QTableWidgetItem(row[2]))
            self.ui.tbl_venta.setItem(tablerow, 3, QTableWidgetItem(str(float(row[3]))))
            self.ui.tbl_venta.setItem(tablerow, 4, QTableWidgetItem(str(float(row[4]))))
            self.ui.tbl_venta.setItem(tablerow, 5, QTableWidgetItem(str(float(row[5]))))
            tablerow += 1
            
    def buscar_detalles(self):
        venta_id = self.ui.line_id_venta.text()
        venta_id = str("'" + venta_id + "'")

        datosB = self.datosTotal.busca_detalles(venta_id)
        i = len(datosB)

        self.ui.tbl_detalles.setRowCount(i)
        tablerow = 0
        for row in datosB:
            self.ui.tbl_detalles.setItem(tablerow, 0, QTableWidgetItem(str(int(row[0]))))
            self.ui.tbl_detalles.setItem(tablerow, 1, QTableWidgetItem(str(int(row[1]))))
            self.ui.tbl_detalles.setItem(tablerow, 2, QTableWidgetItem(row[2]))
            self.ui.tbl_detalles.setItem(tablerow, 3, QTableWidgetItem(str(float(row[3]))))
            self.ui.tbl_detalles.setItem(tablerow, 4, QTableWidgetItem(str(int(row[4]))))
            self.ui.tbl_detalles.setItem(tablerow, 5, QTableWidgetItem(str(float(row[5]))))
            tablerow += 1
        
    def eli_detalles(self):
        if(self.ud.line_can_2.text()==""):
            mensaje = QMessageBox()

            mensaje.setIcon(QMessageBox.Information)

            mensaje.setWindowTitle('Mensaje Informativo')
            mensaje.setText('Ingrese el numero en la linea de texto')

            mensaje.addButton(QMessageBox.Ok)

            respuesta = mensaje.exec_()

            if respuesta == QMessageBox.Ok:
                print('Botón OK presionado.')
        else:
            venta_id = self.datosTotal.lista_ultima_venta()
            venta_id = int(venta_id)
            
            producto = self.ud.line_can_2.text()
            producto = int(producto)
            
            self.datosTotal.eliminar_detalle(venta_id,producto)
            
    def listar_detalles(self):
        venta_id = self.datosTotal.lista_ultima_venta()
        venta_id = int(venta_id)

        datosB = self.datosTotal.busca_detalles(venta_id)
        i = len(datosB)

        self.ud.tbl_detalles1.setRowCount(i)
        tablerow = 0
        for row in datosB:
            self.ud.tbl_detalles1.setItem(tablerow, 0, QTableWidgetItem(str(int(row[0]))))
            self.ud.tbl_detalles1.setItem(tablerow, 1, QTableWidgetItem(str(int(row[1]))))
            self.ud.tbl_detalles1.setItem(tablerow, 2, QTableWidgetItem(row[2]))
            self.ud.tbl_detalles1.setItem(tablerow, 3, QTableWidgetItem(str(float(row[3]))))
            self.ud.tbl_detalles1.setItem(tablerow, 4, QTableWidgetItem(str(int(row[4]))))
            self.ud.tbl_detalles1.setItem(tablerow, 5, QTableWidgetItem(str(float(row[5]))))
            tablerow += 1

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mi_app = MiApp()
    mi_app.show()
    sys.exit(app.exec_())
