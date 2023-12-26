-- Crea la base de datos utilizando UTF-8
CREATE DATABASE IF NOT EXISTS interfaz_de_venta CHARACTER SET utf8 COLLATE utf8_general_ci;

-- Selecciona la base de datos recién creada
USE interfaz_de_venta;

CREATE TABLE venta (
    codigo_venta INT AUTO_INCREMENT PRIMARY KEY,
    comprador_nombre VARCHAR(255) CHARACTER SET utf8 COLLATE utf8_general_ci,
    venta_fecha VARCHAR(10) CHARACTER SET utf8 COLLATE utf8_general_ci,
    venta_monto DOUBLE,
    venta_igv DOUBLE,
    venta_montofinal DOUBLE
);

CREATE TABLE detalle_venta (
	codigo_venta INT,
    producto_id INT,
    producto_nombre VARCHAR(255) CHARACTER SET utf8 COLLATE utf8_general_ci,
    producto_precio DOUBLE,
    producto_cantidad INT,
    producto_total DOUBLE,
    FOREIGN KEY (codigo_venta) REFERENCES venta(codigo_venta),
    primary key(codigo_venta, producto_id)
);    
    