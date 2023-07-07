CREATE TABLE `entrada_repuesto` (
  `id_entrada_repuesto` int(11) NOT NULL AUTO_INCREMENT,
  `id_repuesto` int(11) NOT NULL,
  `cantidad_entrada_repuesto` int(11) NOT NULL,
  `id_proveedor` int(11) NOT NULL,
  `fecha_entrada_repuesto` date NOT NULL,
  PRIMARY KEY (`id_entrada_repuesto`),
  KEY `fk_entrada_repuesto` (`id_repuesto`),
  KEY `fk_proveedor_repuesto` (`id_proveedor`),
  CONSTRAINT `fk_entrada_repuesto` FOREIGN KEY (`id_repuesto`) REFERENCES `registrar_repuesto` (`id_repuesto`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `fk_proveedor_repuesto` FOREIGN KEY (`id_proveedor`) REFERENCES `registrar_proveedor` (`id_proveedor`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

INSERT INTO entrada_repuesto VALUES (2, 11, 5, 2, datetime.date(2023, 6, 20));
INSERT INTO entrada_repuesto VALUES (4, 11, 15, 2, datetime.date(2023, 6, 21));
INSERT INTO entrada_repuesto VALUES (14, 15, 22, 5, datetime.date(2023, 5, 22));
INSERT INTO entrada_repuesto VALUES (15, 15, 22, 4, datetime.date(2023, 6, 9));
INSERT INTO entrada_repuesto VALUES (16, 11, 5, 2, datetime.date(2023, 6, 8));

CREATE TABLE `registrar_proveedor` (
  `id_proveedor` int(11) NOT NULL AUTO_INCREMENT,
  `codigo_proveedor` varchar(4) NOT NULL,
  `ruc_proveedor` bigint(11) NOT NULL,
  `razon_social_proveedor` varchar(255) NOT NULL,
  `telefono_proveedor` varchar(9) NOT NULL,
  `direccion_proveedor` varchar(255) NOT NULL,
  PRIMARY KEY (`id_proveedor`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

INSERT INTO registrar_proveedor VALUES (2, 'P002', 2147483640, 'Paquitoaaaoa', '753410497', 'Chinchaaaa');
INSERT INTO registrar_proveedor VALUES (4, 'P003', 14785296332, 'Paquitakkk', '957496524', 'Icaaa');
INSERT INTO registrar_proveedor VALUES (5, 'P004', 14253674859, 'Una empresa siksi', '741258963', 'Pisco');

CREATE TABLE `registrar_repuesto` (
  `id_repuesto` int(11) NOT NULL AUTO_INCREMENT,
  `codigo_repuesto` varchar(4) NOT NULL,
  `nombre_repuesto` varchar(255) NOT NULL,
  `descripcion_repuesto` varchar(255) NOT NULL,
  `cantidad_minima_repuesto` int(11) NOT NULL,
  `foto_repuesto` blob NOT NULL,
  `cantidad_total` int(11) NOT NULL,
  PRIMARY KEY (`id_repuesto`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

INSERT INTO registrar_repuesto VALUES (9, 'R001', 'ABC', 'ABC', 21, b'static/imgRepuestos\\PESTEL.png', 8);
INSERT INTO registrar_repuesto VALUES (11, 'R003', 'PAE', 'EAP', 17, b"'<FileStorage: 'aa.jpg' ('image/jpeg')>'", 11);
INSERT INTO registrar_repuesto VALUES (15, 'R004', 'Cuchilla', 'Siksi', 10, b'static/imgRepuestos\\Cuchilla.png', 12);

CREATE TABLE `registrar_responsable` (
  `id_responsable` int(11) NOT NULL AUTO_INCREMENT,
  `codigo_responsable` varchar(4) NOT NULL,
  `nombres_responsable` varchar(255) NOT NULL,
  `apellidos_responsable` varchar(255) NOT NULL,
  `telefono_responsable` varchar(9) NOT NULL,
  `direccion_responsable` varchar(255) NOT NULL,
  PRIMARY KEY (`id_responsable`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

INSERT INTO registrar_responsable VALUES (2, 'R002', 'Angel ', 'Cavero Hernandez', '987654321', 'Algun lado :D');

CREATE TABLE `salida_repuesto` (
  `id_salida_repuesto` int(11) NOT NULL AUTO_INCREMENT,
  `id_repuesto` int(11) NOT NULL,
  `cantidad_salida_repuesto` int(11) NOT NULL,
  `id_responsable` int(11) NOT NULL,
  `fecha_salida_repuesto` date NOT NULL,
  PRIMARY KEY (`id_salida_repuesto`),
  KEY `fk_salida_repuesto` (`id_repuesto`),
  KEY `fk_responsable_repuesto` (`id_responsable`),
  CONSTRAINT `fk_responsable_repuesto` FOREIGN KEY (`id_responsable`) REFERENCES `registrar_responsable` (`id_responsable`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `fk_salida_repuesto` FOREIGN KEY (`id_repuesto`) REFERENCES `registrar_repuesto` (`id_repuesto`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=79 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

INSERT INTO salida_repuesto VALUES (1, 11, 15, 2, datetime.date(2023, 2, 25));
INSERT INTO salida_repuesto VALUES (71, 11, 3, 2, datetime.date(2023, 6, 14));
INSERT INTO salida_repuesto VALUES (72, 11, 3, 2, datetime.date(2023, 6, 13));
INSERT INTO salida_repuesto VALUES (73, 11, 3, 2, datetime.date(2023, 6, 12));
INSERT INTO salida_repuesto VALUES (74, 11, 3, 2, datetime.date(2023, 6, 6));
INSERT INTO salida_repuesto VALUES (75, 9, 2, 2, datetime.date(2023, 6, 27));
INSERT INTO salida_repuesto VALUES (76, 11, 10, 2, datetime.date(2023, 6, 20));
INSERT INTO salida_repuesto VALUES (77, 15, 10, 2, datetime.date(2023, 6, 12));

CREATE TABLE `user` (
  `id` smallint(3) unsigned NOT NULL AUTO_INCREMENT,
  `username` varchar(20) NOT NULL,
  `password` char(102) NOT NULL,
  `fullname` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

INSERT INTO user VALUES (1, 'MCANELO', 'pbkdf2:sha256:600000$3bafX3z4hwxuvRpR$ea38cb55baf61f49f34b4176c72f1c9e9efaba26b58acb96f91de9139fd6a713', 'Magaly Canelo');
INSERT INTO user VALUES (3, 'DLEGUA', 'pbkdf2:sha256:600000$iIp0bngH1SR5ovdk$fab7539715a627e0c23b61b4654a514e5fcb36b60657d50580a84f9ac692d54c', 'Danny Legua');
INSERT INTO user VALUES (4, 'MBRAVO', 'pbkdf2:sha256:600000$QI7wcakRV91Er5Fc$fbf0c19a366f86c695a7c1a4bcefca383f04846e736b321eb8e0e2a0f4bbade3', 'Odaliz Bravo Mayuri');
INSERT INTO user VALUES (5, 'FSIGUAS', 'pbkdf2:sha256:600000$QNiQgEa8eFPQXHdK$c55776c36dbcd6d8a7c79e3230c5467df558454195052160a17508e65758087b', 'FLAVIA SIGUAS TORRES');

