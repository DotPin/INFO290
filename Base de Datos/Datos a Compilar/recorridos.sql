-- MySQL dump 10.13  Distrib 5.5.53, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: recorridos
-- ------------------------------------------------------
-- Server version	5.5.53-0ubuntu0.14.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `caracteristicas`
--

DROP TABLE IF EXISTS `caracteristicas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `caracteristicas` (
  `id_caract` int(11) NOT NULL AUTO_INCREMENT,
  `tipo` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id_caract`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `caracteristicas`
--

LOCK TABLES `caracteristicas` WRITE;
/*!40000 ALTER TABLE `caracteristicas` DISABLE KEYS */;
INSERT INTO `caracteristicas` VALUES (1,'Turismo'),(2,'Hospitales/Postas/Clinicas'),(3,'Farmacias'),(4,'Supermercados'),(5,'Municipalidad/Ministerios/Justicia'),(6,'Terminales'),(7,'C.Comerciales/Galerias'),(9,'Universidades'),(10,'Hotel/Hospedajes'),(11,'Restobar/Cafe');
/*!40000 ALTER TABLE `caracteristicas` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `dir_loc`
--

DROP TABLE IF EXISTS `dir_loc`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `dir_loc` (
  `id_direccion` int(11) DEFAULT NULL,
  `patente` varchar(10) DEFAULT NULL,
  KEY `id_direccion` (`id_direccion`),
  KEY `patente` (`patente`),
  CONSTRAINT `dir_loc_ibfk_1` FOREIGN KEY (`id_direccion`) REFERENCES `direcciones` (`id_direccion`),
  CONSTRAINT `dir_loc_ibfk_2` FOREIGN KEY (`patente`) REFERENCES `locomociones` (`patente`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dir_loc`
--

LOCK TABLES `dir_loc` WRITE;
/*!40000 ALTER TABLE `dir_loc` DISABLE KEYS */;
INSERT INTO `dir_loc` VALUES (1,'ACBD43'),(2,'ACBD43'),(3,'ACBD43'),(4,'ACBD43'),(5,'ACBD43'),(6,'ACBD43'),(7,'ACBD43'),(8,'ACBD43'),(9,'ACBD43'),(10,'ACBD43'),(11,'ACBD43'),(12,'ACBD43'),(13,'ACBD43'),(14,'ACBD43'),(15,'ACBD43'),(16,'ACBD43'),(17,'ACBD43'),(18,'ACBD43'),(19,'ACBD43'),(20,'ACBD43'),(21,'ACBD43'),(22,'ACBD43'),(23,'ACBD43'),(24,'ACBD43'),(25,'ACBD43'),(26,'ACBD43'),(27,'ACBD43'),(28,'ACBD43'),(29,'ACBD43'),(30,'ACBD43'),(31,'ACBD43'),(32,'ACBD43'),(33,'CNDO31'),(62,'CNDO31'),(35,'CNDO31'),(36,'CNDO31'),(37,'CNDO31'),(38,'CNDO31'),(39,'CNDO31'),(40,'CNDO31'),(56,'CNDO31'),(42,'CNDO31'),(43,'CNDO31'),(44,'CNDO31'),(8,'CNDO31'),(7,'CNDO31'),(6,'CNDO31'),(28,'CNDO31'),(4,'CNDO31'),(5,'CNDO31'),(45,'ACMP17'),(46,'ACMP17'),(47,'ACMP17'),(48,'ACMP17'),(49,'ACMP17'),(50,'ACMP17'),(51,'ACMP17'),(52,'ACMP17'),(53,'ACMP17'),(54,'ACMP17'),(55,'ACMP17'),(42,'ACMP17'),(10,'ACMP17'),(12,'ACMP17'),(13,'ACMP17'),(14,'ACMP17'),(57,'ACMP17'),(58,'ACMP17'),(22,'ACMP17'),(23,'ACMP17'),(24,'ACMP17'),(25,'ACMP17'),(59,'ACMP17'),(60,'ACMP17'),(61,'ACMP17'),(5,'ACMP17'),(28,'ACMP17'),(31,'ACMP17'),(3,'ACMP17'),(32,'ACMP17'),(40,'MLNK55'),(35,'MLNK55'),(62,'MLNK55'),(33,'MLNK55'),(39,'MLNK55'),(10,'MLNK55'),(63,'MLNK55'),(64,'MLNK55'),(56,'MLNK55'),(65,'MLNK55'),(8,'MLNK55'),(7,'MLNK55'),(6,'MLNK55'),(66,'MLNK55'),(31,'MLNK55'),(3,'MLNK55'),(32,'MLNK55'),(4,'MLNK55'),(5,'MLNK55'),(45,'PLKT32'),(46,'PLKT32'),(47,'PLKT32'),(67,'PLKT32'),(68,'PLKT32'),(69,'PLKT32'),(49,'PLKT32'),(70,'PLKT32'),(71,'PLKT32'),(72,'PLKT32'),(7,'PLKT32'),(6,'PLKT32'),(28,'PLKT32'),(29,'PLKT32'),(4,'PLKT32'),(73,'PLKT32'),(74,'PLKT32'),(75,'PLKT32'),(76,'PLKT32'),(77,'PLKT32'),(17,'PLKT32'),(18,'PLKT32'),(78,'PLKT32'),(91,'PLKT32'),(19,'PLKT32'),(79,'APTR45'),(81,'APTR45'),(80,'APTR45'),(82,'APTR45'),(83,'APTR45'),(84,'APTR45'),(85,'APTR45'),(86,'APTR45'),(87,'APTR45'),(88,'APTR45'),(89,'APTR45'),(90,'APTR45'),(55,'APTR45'),(44,'APTR45'),(8,'APTR45'),(7,'APTR45'),(6,'APTR45'),(66,'APTR45'),(30,'APTR45'),(29,'APTR45'),(4,'APTR45'),(73,'APTR45'),(74,'APTR45'),(75,'APTR45'),(76,'APTR45'),(77,'APTR45'),(17,'APTR45'),(18,'APTR45'),(78,'APTR45'),(91,'APTR45'),(19,'APTR45');
/*!40000 ALTER TABLE `dir_loc` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `direcciones`
--

DROP TABLE IF EXISTS `direcciones`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `direcciones` (
  `id_direccion` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(20) NOT NULL,
  `ciudad` varchar(20) NOT NULL,
  `numero` int(11) DEFAULT NULL,
  `sector` varchar(30) DEFAULT NULL,
  `cod_postal` int(11) DEFAULT NULL,
  PRIMARY KEY (`id_direccion`)
) ENGINE=InnoDB AUTO_INCREMENT=92 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `direcciones`
--

LOCK TABLES `direcciones` WRITE;
/*!40000 ALTER TABLE `direcciones` DISABLE KEYS */;
INSERT INTO `direcciones` VALUES (1,'Niebla','Valdivia',0,'Niebla',0),(2,'Los lingues','Valdivia',0,'Isla Teja',0),(3,'Los Robles','Valdivia',0,'Isla Teja',0),(4,'Independencia','Valdivia',0,'Centro',0),(5,'Arauco','Valdivia',0,'Centro',0),(6,'Picarte','Valdivia',0,'Centro',0),(7,'Picarte','Valdivia',0,'Regional',0),(8,'Picarte','Valdivia',0,'San Luis',0),(9,'Av. Francia','Valdivia',0,'Teniente Merino',0),(10,'Av. Francia','Valdivia',0,'Yañez Savala',0),(11,'Av. Francia','Valdivia',0,'San Luis',0),(12,'Gral. Montecino Caro','Valdivia',0,'Yañez Savala',0),(13,'C.Barrientos','Valdivia',0,'Yañez Savala',0),(14,'Circunvalacion Sur','Valdivia',0,'Yañez Savala',0),(15,'Pedro Montt','Valdivia',0,'Los Fundadores',0),(16,'Intendente Luis Dama','Valdivia',0,'Los Fundadores',0),(17,'Camino A.Angachilla','Valdivia',0,'Guacamayo',0),(18,'Ing. Raul Saez Saez','Valdivia',0,'Guacamayo',0),(19,'Ing. Federico Weise','Valdivia',0,'Guacamayo',0),(20,'Circunvalacion Sur','Valdivia',0,'El Bosque',0),(21,'Simpson','Valdivia',0,'El Bosque',0),(22,'Simpson','Valdivia',0,'Regional',0),(23,'Havdaerbeck','Valdivia',0,'Regional',0),(24,'Anibal Pinto','Valdivia',0,'Regional',0),(25,'Anibal Pinto','Valdivia',0,'Barrios Bajos',0),(26,'Bauchef','Valdivia',0,'Centro',0),(27,'Esmeralda','Valdivia',0,'Centro',0),(28,'Garcia Reyes','Valdivia',0,'Centro',0),(29,'Chacabuco','Valdivia',0,'Centro',0),(30,'Carapagne','Valdivia',0,'Centro',0),(31,'Carampangue','Valdivia',0,'Centro',0),(32,'Los Laureles','Valdivia',0,'Uach',0),(33,'Intendente Luis Dama','Valdivia',0,'La Estancia',0),(34,'A.Jose Manuel Torres','Valdivia',0,'La Estancia',0),(35,'A.Ricardo Barahona','Valdivia',0,'La Estancia',0),(36,'Pedro Montt','Valdivia',0,'La Estancia',0),(37,'R.Roberto Fernandez ','Valdivia',0,'La Estancia',0),(38,'A.Juan Manuel Lorca','Valdivia',0,'La Estancia',0),(39,'A.Jorge Bustos','Valdivia',0,'La Estancia',0),(40,'Rene Schneider','Valdivia',0,'La Estancia',0),(42,'Rene Schneider','Valdivia',0,'Teniente Merino',0),(43,'Ruben Dario','Valdivia',0,'Teniente Merino',0),(44,'Picarte','Valdivia',0,'Teniente Merino',0),(45,'Balmaceda','Valdivia',0,'Collico',0),(46,'Circunvalacion Orien','Valdivia',0,'Ines de Suarez',0),(47,'Uruguay','Valdivia',0,'Ines de Suarez',0),(48,'Colombia','Valdivia',0,'Ines de Suarez',0),(49,'Las Camelias','Valdivia',0,'Ines de Suarez',0),(50,'Argentina','Valdivia',0,'Ines de Suarez',0),(51,'Dn. Holzapfel','Valdivia',0,'Ines de Suarez',0),(52,'Dn. Holzapfel','Valdivia',0,'La Corvi',0),(53,'Jose Victorino Lasta','Valdivia',0,'La Corvi',0),(54,'Martinez de Rozas','Valdivia',0,'La Corvi',0),(55,'Ruben Dario','Valdivia',0,'La Corvi',0),(56,'Rene Schneider','Valdivia',0,'San Luis',0),(57,'Pedro Montt','Valdivia',0,'Yañez Savala',0),(58,'Av. Francia','Valdivia',0,'Regional',0),(59,'Lord Cochrane','Valdivia',0,'Barrios Bajos',0),(60,'Perez Rosales','Valdivia',0,'Barrios Bajos',0),(61,'Perez Rosales','Valdivia',0,'Centro',0),(62,'A.Jose Maria Torres ','Valdivia',0,'La Estancia',0),(63,'San Luis','Valdivia',0,'San Luis',0),(64,'Carlos Hilker','Valdivia',0,'San Luis',0),(65,'Manuel Caceres','Valdivia',0,'San Luis',0),(66,'Alemania','Valdivia',0,'Centro',0),(67,'Geranios','Valdivia',0,'Ines de Suarez',0),(68,'Los Girasoles','Valdivia',0,'Ines de Suarez',0),(69,'Gladiolos','Valdivia',0,'Ines de Suarez',0),(70,'Viña del Mar','Valdivia',0,'Ines de Suarez',0),(71,'Patricio Lynch','Valdivia',0,'Barrio Estacion',0),(72,'Picarte','Valdivia',0,'Barrio Estacion',0),(73,'Maipu','Valdivia',0,'Centro',0),(74,'Yungay','Valdivia',0,'Centro',0),(75,'Gral.Lagos','Valdivia',0,'Barrios Bajos',0),(76,'Francisco Bilbao','Valdivia',0,'Barrios Bajos',0),(77,'Arica','Valdivia',0,'Miraflores',0),(78,'Pase los Naranjos','Valdivia',0,'Guacamayo',0),(79,'Picarte','Valdivia',0,'Picarte 3000',0),(80,'Volcan Puyehue','Valdivia',0,'Sector Sur',0),(81,'Circunvalacion Sur','Valdivia',0,'Sector Sur',0),(82,'Volcan Villarrica','Valdivia',0,'Sector Sur',0),(83,'Principe Felipe','Valdivia',0,'Sector Sur',0),(84,'Rey Juan Carlos','Valdivia',0,'Sector Sur',0),(85,'Errazuriz','Valdivia',0,'Sector Sur',0),(86,'Los Corregidores','Valdivia',0,'Sector Sur',0),(87,'Ignacio de la Carrer','Valdivia',0,'Picarte 3000',0),(88,'Donald Canter','Valdivia',0,'Picarte 3000',0),(89,'Alonso Villanueva','Valdivia',0,'Picarte 3000',0),(90,'Rio Cau-Cau','Valdivia',0,'Picarte 3000',0),(91,'Intendente Luis Dama','Valdivia',0,'Guacamayo',0);
/*!40000 ALTER TABLE `direcciones` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `locomociones`
--

DROP TABLE IF EXISTS `locomociones`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `locomociones` (
  `patente` varchar(10) NOT NULL,
  `tipo` varchar(20) NOT NULL,
  `linea` tinyint(4) DEFAULT NULL,
  `h_inicio` time DEFAULT NULL,
  `h_final` time DEFAULT NULL,
  `discapacitados` bit(1) DEFAULT NULL,
  PRIMARY KEY (`patente`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `locomociones`
--

LOCK TABLES `locomociones` WRITE;
/*!40000 ALTER TABLE `locomociones` DISABLE KEYS */;
INSERT INTO `locomociones` VALUES ('ACBD43','Microbus',20,'07:30:00','20:30:00','\0'),('ACMP17','Microbus',5,'07:30:00','20:30:00','\0'),('APTR45','Microbus',3,'07:30:00','20:30:00','\0'),('CNDO31','Microbus',11,'07:30:00','20:30:00','\0'),('MLNK55','Microbus',14,'07:30:00','20:30:00','\0'),('PLKT32','Microbus',1,'07:30:00','20:30:00','\0');
/*!40000 ALTER TABLE `locomociones` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `lug_car`
--

DROP TABLE IF EXISTS `lug_car`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `lug_car` (
  `id_lugar` int(11) DEFAULT NULL,
  `id_caract` int(11) DEFAULT NULL,
  KEY `id_lugar` (`id_lugar`),
  KEY `id_caract` (`id_caract`),
  CONSTRAINT `lug_car_ibfk_1` FOREIGN KEY (`id_lugar`) REFERENCES `lugares` (`id_lugar`),
  CONSTRAINT `lug_car_ibfk_2` FOREIGN KEY (`id_caract`) REFERENCES `caracteristicas` (`id_caract`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `lug_car`
--

LOCK TABLES `lug_car` WRITE;
/*!40000 ALTER TABLE `lug_car` DISABLE KEYS */;
INSERT INTO `lug_car` VALUES (1,1),(2,1),(3,1),(4,1),(5,1),(6,1),(7,1),(8,1),(9,1),(10,1),(11,1),(12,1),(13,1),(14,1),(15,1),(16,1),(17,4),(18,4),(19,4),(20,4),(21,4),(22,4),(23,4),(24,4),(25,5),(26,5),(27,5),(28,5),(29,5),(30,5),(31,5),(32,5),(33,2),(34,2),(35,2),(36,2),(37,2),(38,2),(39,2),(40,11),(41,11),(42,11),(43,11),(44,11),(45,11),(46,11),(47,11),(48,11),(49,3),(50,3),(51,3),(52,6),(53,6),(54,7),(55,7),(56,7),(57,7),(58,7),(59,10),(60,10),(61,10),(62,10),(63,10),(64,10),(65,9),(66,9),(67,9),(68,9);
/*!40000 ALTER TABLE `lug_car` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `lug_dir`
--

DROP TABLE IF EXISTS `lug_dir`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `lug_dir` (
  `id_lugar` int(11) DEFAULT NULL,
  `id_direccion` int(11) DEFAULT NULL,
  KEY `id_lugar` (`id_lugar`),
  KEY `id_direccion` (`id_direccion`),
  CONSTRAINT `lug_dir_ibfk_1` FOREIGN KEY (`id_lugar`) REFERENCES `lugares` (`id_lugar`),
  CONSTRAINT `lug_dir_ibfk_2` FOREIGN KEY (`id_direccion`) REFERENCES `direcciones` (`id_direccion`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `lug_dir`
--

LOCK TABLES `lug_dir` WRITE;
/*!40000 ALTER TABLE `lug_dir` DISABLE KEYS */;
INSERT INTO `lug_dir` VALUES (1,1),(2,1),(3,3),(3,4),(4,7),(5,75),(6,3),(6,32),(7,4),(7,29),(8,5),(9,4),(9,73),(10,6),(11,21),(12,3),(13,64),(14,3),(15,32),(16,51),(16,52),(17,51),(17,52),(18,44),(18,8),(19,44),(19,8),(20,28),(20,6),(21,29),(21,30),(22,79),(22,55),(23,20),(23,21),(24,5),(24,28),(25,4),(25,29),(26,6),(27,66),(28,66),(29,74),(30,6),(31,24),(32,5),(33,58),(33,22),(34,10),(35,40),(36,9),(36,11),(37,42),(38,8),(39,26),(40,27),(41,27),(42,4),(43,29),(44,61),(44,6),(45,61),(46,61),(47,31),(48,6),(48,5),(49,6),(49,23),(50,6),(51,6),(51,21),(51,20),(52,66),(52,6),(53,29),(54,5),(55,5),(55,26),(56,6),(57,74),(58,74),(59,66),(59,31),(60,66),(60,31),(60,74),(61,74),(62,66),(62,31),(62,28),(63,23),(64,75),(65,6),(66,75),(67,75),(68,32);
/*!40000 ALTER TABLE `lug_dir` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `lugares`
--

DROP TABLE IF EXISTS `lugares`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `lugares` (
  `id_lugar` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(20) NOT NULL,
  `descripcion` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id_lugar`)
) ENGINE=InnoDB AUTO_INCREMENT=69 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `lugares`
--

LOCK TABLES `lugares` WRITE;
/*!40000 ALTER TABLE `lugares` DISABLE KEYS */;
INSERT INTO `lugares` VALUES (1,'Niebla','Localidad de Valdivia camino al mar'),(2,'Corral','Localidad de Niebla camino al mar'),(3,'Mercado Fluvial','Sector de pescadores artesanales en costanera valdivia'),(4,'Torreon 1','Monumento Historico de la epoca colonial, Valdivia'),(5,'Torreon 2','Monumento Historico de la epoca colonial, Valdivia'),(6,'Museo','Muestra de objetos, momias, documentos, fosiles y arte historico de valdivia'),(7,'Teatro','Escenario de obras teatrales'),(8,'Cine','Salas de proyeccion de peliculas'),(9,'Plaza Republica','Plaza principal de Valdivia'),(10,'Plaza Simon Bolivar','Plaza frente coliseo'),(11,'Parque Urbano El Bos','Parque de selva valdiviana urbana'),(12,'Parque Prochelle','Parque pasando el puente calle-calle'),(13,'Parque Krammer','Parque que rodea uno de los humedales de valdivia'),(14,'Parque Sta. Ines','Parque en sector isla teja camino niebla'),(15,'Jardin Botanico UACH','Jardin dentro de la Universidad Austral'),(16,'Piscina AQUA','Piscina publica temperada de valdivia'),(17,'Puritan','Supermercado del sector Corvi'),(18,'Mayorista 10','Supermercado Bodega'),(19,'Acuenta','Supermercado Bodega'),(20,'Lider Express','Supermercado Retail'),(21,'Santa Isabel 1','Supermercado Retail'),(22,'Santa Isabel 2','Supermercado Retail'),(23,'El Trebol','Supermercado local del Sector El Bosque'),(24,'Unimarc','Supermercado Retail'),(25,'Municipalidad de Val','Municipio de la Ciudad de Valdivia, capital de la region'),(26,'Gobernacion','Departamento del municipio'),(27,'Seremi de Educacion','Departamento del ministerio de educacion'),(28,'Sernatur','Departamento de la cultura del gobierno regional'),(29,'Corte de Apelaciones','Tribunal de justicia chileno'),(30,'Registro Civil','Registro de la sociedad civil del pais'),(31,'Juzgado de Familia','tribunal de justicia familiar'),(32,'Primera Comisaria','Comisaria de policia local'),(33,'Hospital Base','Hospital base de la region de los rios'),(34,'Consultorio Externo ','Centro de salud primario sector Yañez Savala'),(35,'Centro de Salud Fami','Centro de salud primario sector San Pedro'),(36,'Teleton','Centro de rehabilitacion'),(37,'Centro de Salud Ment','Centro de salud psicologico/psiquiatrico de valdivia'),(38,'Centro de Salud Fami','Centro de atencion primaria, sector Teniente Merino/San Luis'),(39,'Clinica Alemana','Centro de salud privado de Valdivia'),(40,'Cover','Restaurant y cerveceria'),(41,'New Orleans','Restaurant y cerveceria'),(42,'Cafe Moro','Cafe, colaciones, postres, desayunos y cervezas'),(43,'Cafe Da Hauss','Cafe, colaciones, postres, desayunos y cervezas'),(44,'Cafe Palace','Cafe, colaciones, postres, desayunos, tragos y cervezas'),(45,'Cafe EntreLagos','Cafe, colaciones, postres, desayunos y chocolateria surtida'),(46,'Ultima Frontera','Resutaurant, cerveceria, colaciones y demases'),(47,'Strike','Resutaurant, cerveceria, tragos, karaoques, fiestas'),(48,'Cafe Cicle','Cafe, colaciones, postres, desayunos, taller mecanico de bicicletas y repuestos'),(49,'Cruz Verde','farmacias de turno'),(50,'Salco Brand','farmacias de turno'),(51,'Ahumada','farmacias de turno'),(52,'Terminal de Valdivia','Estacion de buses principal de valdivia'),(53,'Terminal InterUrbano','Estacion de buses interUrbano de Valdivia'),(54,'Centro Comercial Ara','Centro de locales comerciales ubicado en calle arauco'),(55,'Mall de Valdivia','Centro de locales reail del pais, principal de valdivia'),(56,'Galeria Cristal','Galeria con locales comerciales locales de la zona'),(57,'Mercado Municipal','centro de locales de comidas y desayunos de la zona'),(58,'Feria Artesanal','Locales de articulos artesanales de la zona'),(59,'Hostal Casa Grande','residencia esporadica para visitas'),(60,'Hotel Dreams','Residencia frente al casino de valdivia'),(61,'Hostal del Muelle','residencia esporadica para visitas'),(62,'Hotel Melillanca','Hotel de categoria de valdivia'),(63,'Hotel Naguilan','Hotel de categoria de valdivia'),(64,'Apart Home Casa Blan','Cabañas para alojo en valdivia'),(65,'U. San Sebastian','Universidad privada '),(66,'U. Santo Tomas','Universidad privada '),(67,'UACH Miraflores','Universidad privada de Valdivia, campus Miraflores'),(68,'UACH Teja','Universidad privada de Valdivia, campus Isla Teja');
/*!40000 ALTER TABLE `lugares` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `usr_lug`
--

DROP TABLE IF EXISTS `usr_lug`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `usr_lug` (
  `id_usr` int(11) DEFAULT NULL,
  `id_lugar` int(11) DEFAULT NULL,
  `valoracion` decimal(2,1) DEFAULT NULL,
  KEY `id_usr` (`id_usr`),
  KEY `id_lugar` (`id_lugar`),
  CONSTRAINT `usr_lug_ibfk_1` FOREIGN KEY (`id_usr`) REFERENCES `usuarios` (`id_usr`),
  CONSTRAINT `usr_lug_ibfk_2` FOREIGN KEY (`id_lugar`) REFERENCES `lugares` (`id_lugar`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usr_lug`
--

LOCK TABLES `usr_lug` WRITE;
/*!40000 ALTER TABLE `usr_lug` DISABLE KEYS */;
INSERT INTO `usr_lug` VALUES (1,20,5.0),(1,12,4.5),(1,2,5.0),(1,2,9.9),(1,4,4.6),(1,6,4.6),(1,13,4.6),(1,11,4.6),(1,9,4.6),(1,5,4.6),(1,17,4.6),(1,34,4.6),(1,43,4.6),(1,53,4.6),(1,45,4.6),(1,25,4.6),(1,53,4.6),(1,53,6.7),(1,61,6.7),(1,65,6.7),(1,15,6.7),(2,15,3.2),(2,11,3.2),(2,12,5.2),(2,16,5.6),(2,23,4.6),(2,26,4.6),(2,26,4.9),(2,31,3.9),(2,34,6.9),(2,41,7.9),(2,45,7.9),(2,57,9.1),(2,56,9.4),(3,56,2.4),(3,34,2.4),(3,42,5.4),(3,43,5.3),(3,31,3.3),(3,32,3.5),(3,54,9.9),(3,45,3.5),(3,65,6.5),(3,68,6.5),(3,63,6.4),(3,56,6.4),(3,17,6.4),(3,41,6.4),(3,32,6.4),(3,51,6.4),(3,24,6.4),(3,27,6.4),(3,64,6.6),(7,44,6.6),(7,34,5.6),(7,32,5.6),(7,1,5.6),(7,3,5.6),(7,5,5.6),(7,9,4.6),(7,2,4.9),(7,2,3.0),(7,4,5.0),(7,12,8.0),(7,15,9.0),(7,26,9.0),(7,44,9.0),(7,61,9.0),(7,56,4.0),(7,47,7.4),(7,57,7.4),(8,45,7.4),(8,45,7.2),(8,43,7.2),(8,23,7.2),(8,34,7.2),(8,32,2.2),(8,41,2.5),(8,1,4.5),(8,4,4.5),(8,3,3.5),(8,3,3.7),(8,5,3.7),(8,7,3.6),(8,9,5.6),(8,19,5.6),(8,28,4.6),(8,36,3.6);
/*!40000 ALTER TABLE `usr_lug` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `usuarios`
--

DROP TABLE IF EXISTS `usuarios`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `usuarios` (
  `id_usr` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(20) DEFAULT NULL,
  `a_paterno` varchar(20) DEFAULT NULL,
  `a_materno` varchar(20) DEFAULT NULL,
  `correo` varchar(20) NOT NULL,
  `apodo` varchar(20) NOT NULL,
  PRIMARY KEY (`id_usr`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usuarios`
--

LOCK TABLES `usuarios` WRITE;
/*!40000 ALTER TABLE `usuarios` DISABLE KEYS */;
INSERT INTO `usuarios` VALUES (1,'Alam','Brito','','asd@ds.com','lolo'),(2,'Cone','Trato','','aqw@de.com','lolasd'),(3,'Heli','Coptero','','qwc@dga.com','palito'),(4,'Cole','Tazo','','pkm@dpl.com','coe'),(5,'Cintia','Pozo','','ggl@hg.com','pati'),(6,'Catalina','Coco','','sdl@ga.com','Cata'),(7,'Kato','Benzo','','hhkl@ppd.com','Ponce'),(8,'Rigby','Ponce','','asd@pqba.com','Rigby'),(9,'Bara','Prita','','asd@pqba.com','Palo');
/*!40000 ALTER TABLE `usuarios` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2016-12-18 18:20:54
