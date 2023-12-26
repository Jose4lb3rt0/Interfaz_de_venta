# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'detalles.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_FormDetalles(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(754, 715)
        Form.setStyleSheet("background-color: rgb(110, 136, 161);")
        self.line_pro = QtWidgets.QLineEdit(Form)
        self.line_pro.setGeometry(QtCore.QRect(240, 149, 201, 31))
        self.line_pro.setStyleSheet("QLineEdit {\n"
"    border: 2px solid gray; /* Borde*/\n"
"    border-radius: 5px; /* Esquinas redondeadas */\n"
"    padding: 5px; /* Espaciado interno */\n"
"    background-color: rgb(84, 84, 84); /* Fondo gris claro */\n"
"       color: rgb(255, 255, 255); /* Color del texto */\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid #45a049; /* Cambio de color del borde al obtener el foco */\n"
"}\n"
"")
        self.line_pro.setObjectName("line_pro")
        self.label_11 = QtWidgets.QLabel(Form)
        self.label_11.setGeometry(QtCore.QRect(70, 240, 151, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("color: white;")
        self.label_11.setObjectName("label_11")
        self.line_can = QtWidgets.QLineEdit(Form)
        self.line_can.setGeometry(QtCore.QRect(240, 230, 113, 31))
        self.line_can.setStyleSheet("QLineEdit {\n"
"    border: 2px solid gray; /* Borde*/\n"
"    border-radius: 5px; /* Esquinas redondeadas */\n"
"    padding: 5px; /* Espaciado interno */\n"
"    background-color: rgb(84, 84, 84); /* Fondo gris claro */\n"
"        color: rgb(255, 255, 255); /* Color del texto */\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid #45a049; /* Cambio de color del borde al obtener el foco */\n"
"}\n"
"")
        self.line_can.setObjectName("line_can")
        self.line_id = QtWidgets.QLineEdit(Form)
        self.line_id.setGeometry(QtCore.QRect(240, 109, 113, 31))
        self.line_id.setStyleSheet("QLineEdit {\n"
"    border: 2px solid gray; /* Borde*/\n"
"    border-radius: 5px; /* Esquinas redondeadas */\n"
"    padding: 5px; /* Espaciado interno */\n"
"    background-color: rgb(84, 84, 84); /* Fondo gris claro */\n"
"    color: rgb(255, 255, 255); /* Color del texto */\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid #45a049; /* Cambio de color del borde al obtener el foco */\n"
"}\n"
"d")
        self.line_id.setObjectName("line_id")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(70, 160, 141, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: white;")
        self.label_5.setObjectName("label_5")
        self.line_pre = QtWidgets.QLineEdit(Form)
        self.line_pre.setGeometry(QtCore.QRect(240, 189, 113, 31))
        self.line_pre.setStyleSheet("QLineEdit {\n"
"    border: 2px solid gray; /* Borde*/\n"
"    border-radius: 5px; /* Esquinas redondeadas */\n"
"    padding: 5px; /* Espaciado interno */\n"
"    background-color: rgb(84, 84, 84); /* Fondo gris claro */\n"
"       color: rgb(255, 255, 255); /* Color del texto */\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid #45a049; /* Cambio de color del borde al obtener el foco */\n"
"}\n"
"")
        self.line_pre.setObjectName("line_pre")
        self.label_10 = QtWidgets.QLabel(Form)
        self.label_10.setGeometry(QtCore.QRect(70, 200, 141, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("color: white;")
        self.label_10.setObjectName("label_10")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(70, 120, 141, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: white;")
        self.label_4.setObjectName("label_4")
        self.btn_det = QtWidgets.QPushButton(Form)
        self.btn_det.setGeometry(QtCore.QRect(540, 150, 141, 61))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.btn_det.setFont(font)
        self.btn_det.setStyleSheet("background-color: rgb(0, 198, 145);\n"
"color: white;\n"
"border-radius: 10px;")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("iconos/agregar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_det.setIcon(icon)
        self.btn_det.setObjectName("btn_det")
        self.tbl_detalles1 = QtWidgets.QTableWidget(Form)
        self.tbl_detalles1.setGeometry(QtCore.QRect(70, 330, 611, 351))
        self.tbl_detalles1.setStyleSheet("QWidget {\n"
"    background-color: rgb(112, 112, 112);\n"
"    color: #fffff8;\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color: rgb(85, 85, 85);\n"
"    padding: 2px;\n"
"    border: 1px solid #fffff8;\n"
"    font-size: 9pt;\n"
"}\n"
"\n"
"QTableWidget {\n"
"    gridline-color: #fffff8;\n"
"    font-size: 12pt;\n"
"}\n"
"\n"
"QTableWidget QTableCornerButton::section {\n"
"    background-color: #646464;\n"
"    border: 1px solid #fffff8;\n"
"}")
        self.tbl_detalles1.setObjectName("tbl_detalles1")
        self.tbl_detalles1.setColumnCount(6)
        self.tbl_detalles1.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_detalles1.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_detalles1.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_detalles1.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_detalles1.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_detalles1.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_detalles1.setHorizontalHeaderItem(5, item)
        self.line_can_2 = QtWidgets.QLineEdit(Form)
        self.line_can_2.setGeometry(QtCore.QRect(380, 290, 171, 31))
        self.line_can_2.setStyleSheet("QLineEdit {\n"
"    border: 2px solid gray; /* Borde*/\n"
"    border-radius: 5px; /* Esquinas redondeadas */\n"
"    padding: 5px; /* Espaciado interno */\n"
"    background-color: rgb(84, 84, 84); /* Fondo gris claro */\n"
"    color: rgb(255, 255, 255); /* Color del texto */\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid #45a049; /* Cambio de color del borde al obtener el foco */\n"
"}\n"
"")
        self.line_can_2.setText("")
        self.line_can_2.setObjectName("line_can_2")
        self.label_12 = QtWidgets.QLabel(Form)
        self.label_12.setGeometry(QtCore.QRect(70, 300, 301, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("color: white;")
        self.label_12.setObjectName("label_12")
        self.btn_eli = QtWidgets.QPushButton(Form)
        self.btn_eli.setGeometry(QtCore.QRect(570, 290, 111, 23))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btn_eli.setFont(font)
        self.btn_eli.setStyleSheet("background-color: rgb(255,255,255);\n"
"color: black;\n"
"border-radius: 10px;")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("iconos/x-mark.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_eli.setIcon(icon1)
        self.btn_eli.setObjectName("btn_eli")
        self.label_15 = QtWidgets.QLabel(Form)
        self.label_15.setGeometry(QtCore.QRect(40, 30, 381, 51))
        font = QtGui.QFont()
        font.setFamily("Forte")
        font.setPointSize(36)
        self.label_15.setFont(font)
        self.label_15.setStyleSheet("color: white;")
        self.label_15.setObjectName("label_15")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_11.setText(_translate("Form", "Cantidad del producto:"))
        self.label_5.setText(_translate("Form", "Nombre del producto:"))
        self.label_10.setText(_translate("Form", "Precio del producto:"))
        self.label_4.setText(_translate("Form", "ID del producto:"))
        self.btn_det.setText(_translate("Form", "Agregar Detalles"))
        item = self.tbl_detalles1.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Codigo_venta"))
        item = self.tbl_detalles1.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Producto_id"))
        item = self.tbl_detalles1.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Producto_nombre"))
        item = self.tbl_detalles1.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Producto_precio"))
        item = self.tbl_detalles1.horizontalHeaderItem(4)
        item.setText(_translate("Form", "Producto_cantidad"))
        item = self.tbl_detalles1.horizontalHeaderItem(5)
        item.setText(_translate("Form", "Producto_Total"))
        self.label_12.setText(_translate("Form", "Ingrese el codigo del producto que eliminara:"))
        self.btn_eli.setText(_translate("Form", "Eliminar"))
        self.label_15.setText(_translate("Form", "Agregar detalles:"))


if __name__ == "__main__":
    import sys
    app1 = QtWidgets.QApplication(sys.argv)
    Form1 = QtWidgets.QWidget()
    ud = Ui_FormDetalles()
    ud.setupUi(Form1)
    Form1.show()
    sys.exit(app1.exec_())
