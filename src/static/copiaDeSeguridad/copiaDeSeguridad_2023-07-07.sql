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
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

INSERT INTO entrada_repuesto VALUES (20, 10, 8, 1, datetime.date(2023, 7, 8));

CREATE TABLE `registrar_proveedor` (
  `id_proveedor` int(11) NOT NULL AUTO_INCREMENT,
  `codigo_proveedor` varchar(4) NOT NULL,
  `ruc_proveedor` bigint(11) NOT NULL,
  `razon_social_proveedor` varchar(255) NOT NULL,
  `telefono_proveedor` varchar(9) NOT NULL,
  `direccion_proveedor` varchar(255) NOT NULL,
  PRIMARY KEY (`id_proveedor`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

INSERT INTO registrar_proveedor VALUES (1, 'P001', 21474814450, 'Elara', '963214752', 'El Carmen - Chincha');
INSERT INTO registrar_proveedor VALUES (3, 'P003', 14253674859, 'Providencia', '954123624', 'Las Americas - Pisco');
INSERT INTO registrar_proveedor VALUES (4, 'P004', 14145896325, 'EdiLar', '914175255', 'Calle San Luis - Pisco');
INSERT INTO registrar_proveedor VALUES (5, 'P005', 25885225885, 'Cravioto', '985471245', 'Av Medrano - Pisco');
INSERT INTO registrar_proveedor VALUES (6, 'P006', 87541236251, 'RTG', '985632145', 'Av. Mariscal Avelino Caceres');
INSERT INTO registrar_proveedor VALUES (7, 'P007', 14245568455, 'No sep', '985554444', 'kmlkmlk');

CREATE TABLE `registrar_repuesto` (
  `id_repuesto` int(11) NOT NULL AUTO_INCREMENT,
  `codigo_repuesto` varchar(4) NOT NULL,
  `nombre_repuesto` varchar(255) NOT NULL,
  `descripcion_repuesto` varchar(255) NOT NULL,
  `cantidad_minima_repuesto` int(11) NOT NULL,
  `foto_repuesto` blob NOT NULL,
  `cantidad_total` int(11) NOT NULL,
  PRIMARY KEY (`id_repuesto`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

INSERT INTO registrar_repuesto VALUES (10, 'R001', 'Cuchilla de corte de cuero', 'Cuchilla de acero inoxidable, marca Daap International.', 22, b"'Cuchilla de corte de cuero.png'", 72);
INSERT INTO registrar_repuesto VALUES (12, 'R003', 'Rodamiento de bolas', 'De alta velocidad y bajo ruido, marca SilentRoll', 17, b'Rodamiento de bolas.png', 22);
INSERT INTO registrar_repuesto VALUES (14, 'R005', 'Filtro de aire', 'De alta eficiencia con carbón activado, marca AirPure.', 36, b"'Filtro de aire.png'", 35);
INSERT INTO registrar_repuesto VALUES (19, 'R006', 'Elemento calefactor', 'Resistencia eléctrica de cerámica, marca HeatPro', 28, b"'Elemento calefactor.png'", 15);

CREATE TABLE `registrar_responsable` (
  `id_responsable` int(11) NOT NULL AUTO_INCREMENT,
  `codigo_responsable` varchar(4) NOT NULL,
  `nombres_responsable` varchar(255) NOT NULL,
  `apellidos_responsable` varchar(255) NOT NULL,
  `telefono_responsable` varchar(9) NOT NULL,
  `direccion_responsable` varchar(255) NOT NULL,
  PRIMARY KEY (`id_responsable`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

INSERT INTO registrar_responsable VALUES (3, 'R003', 'Rocio Andrea', 'Lopez Sanchez', '985474523', 'Calle Salaverry');
INSERT INTO registrar_responsable VALUES (4, 'R004', 'Aiiuda', 'Porque sip', '985555456', 'Algun lado');

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
) ENGINE=InnoDB AUTO_INCREMENT=85 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

INSERT INTO salida_repuesto VALUES (84, 10, 6, 3, datetime.date(2023, 7, 12));

CREATE TABLE `user` (
  `id` smallint(3) unsigned NOT NULL AUTO_INCREMENT,
  `username` varchar(20) NOT NULL,
  `password` char(102) NOT NULL,
  `fullname` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

INSERT INTO user VALUES (6, 'ADMIN', 'pbkdf2:sha256:600000$ijtbxNLfDv5pwyhk$9af2d80b25066c76e3d5a45a97dfade041815cedb550077e04549ce9e45cfb51', 'Administrador');
INSERT INTO user VALUES (7, 'MCANELO', 'pbkdf2:sha256:600000$gZ1JaPgnOwVda8sX$1320a92de776f58335cd13883130d71c76b5e487ed736636c61f7ceeaa3f1c06', 'Magaly Canelo');
INSERT INTO user VALUES (8, 'MCANELO', 'pbkdf2:sha256:600000$wpf6MynOY7XBT0lH$d24a8593750bd2b321790631dcd3fcd8cb45815043240c9b82e4852b0848391c', 'Magaly Canelo');

