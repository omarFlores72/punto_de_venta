-- 1. Tabla de Inventario
CREATE TABLE "inventario" (
	"id"	INTEGER NOT NULL,
	"nombre"	TEXT NOT NULL,
	"proveedor"	TEXT,
	"precio"	REAL NOT NULL,
	"costo"	REAL NOT NULL,
	"stock"	INTEGER NOT NULL,
	"categoria"	TEXT NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);

-- 2. Tabla de Clientes
CREATE TABLE "cliente" (
	"id"	INTEGER NOT NULL,
	"nombre"	TEXT NOT NULL,
	"cedula"	NUMERIC,
	"celular"	NUMERIC,
	"direccion"	TEXT,
	"correo"	TEXT,
	PRIMARY KEY("id" AUTOINCREMENT)
);

-- 3. Tabla de Ventas
-- Nota: 'factura' no es llave primaria porque una factura puede tener múltiples productos (filas)
CREATE TABLE "ventas" (
	"factura"	INTEGER NOT NULL,
	"cliente"	TEXT NOT NULL,
	"producto"	TEXT NOT NULL,
	"precio"	REAL NOT NULL,
	"cantidad"	INTEGER NOT NULL,
	"total"	REAL NOT NULL,
	"fecha"	TEXT NOT NULL,
	"hora"	TEXT NOT NULL,
	"costo"	REAL NOT NULL
);

-- 4. Tabla de Usuarios (Login)
CREATE TABLE "usuarios" (
	"id"	INTEGER NOT NULL,
	"usuario"	TEXT NOT NULL,
	"password"	TEXT NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
); 