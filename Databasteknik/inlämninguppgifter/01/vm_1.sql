-- -----------------------------------------------------
-- DATABASE VM
-- -----------------------------------------------------
CREATE DATABASE IF NOT EXISTS `VM` ;
USE `VM` ;

-- -----------------------------------------------------
-- Table `VM`.`grupp`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `VM`.`grupp` (
  `namn` CHAR(1) NOT NULL,
  PRIMARY KEY (`namn`)
  
) ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `VM`.`lager`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `VM`.`lager` (
  `namn` VARCHAR(255) NOT NULL,
  `grupp_namn` CHAR(1) NOT NULL,
  PRIMARY KEY (`namn`, `grupp_namn`),
  INDEX `fk_lager_grupp_idx` (`grupp_namn` ASC) VISIBLE,
  CONSTRAINT `fk_lager_grupp`
    FOREIGN KEY (`grupp_namn`)
    REFERENCES `VM`.`grupp` (`namn`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
    
) ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `VM`.`Domare`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `VM`.`Domare` (
  `namn` VARCHAR(255) NOT NULL,
  `efternamn` VARCHAR(255) NOT NULL,
  `land` VARCHAR(255) NOT NULL,
  `id` INT NOT NULL,
  PRIMARY KEY (`id`)
  
) ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `VM`.`Stadium`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `VM`.`Stadium` (
  `namn` VARCHAR(255) NOT NULL,
  `stad` VARCHAR(255) NOT NULL,
  `kapacitet` VARCHAR(255) NOT NULL,
  `id` INT NOT NULL,
  PRIMARY KEY (`id`)
  
) ENGINE = InnoDB;



-- -----------------------------------------------------
-- Table `VM`.`match`
-- -----------------------------------------------------

CREATE TABLE IF NOT EXISTS `VM`.`match` (

  `id` INT NOT NULL,
  `n_match` INT NOT NULL,
  `stadium_id` INT NOT NULL,
  `datum` DATE NOT NULL,
  `Domare_id` INT NOT NULL,
  `lager_namn` VARCHAR(255) NOT NULL,
  `poang` INT(1) DEFAULT 0,
  `gjorda_mål` INT DEFAULT 0,
  `insläppta_mål` INT DEFAULT 0,
  PRIMARY KEY (`id`, `stadium_id`, `Domare_id`, `lager_namn`),
  INDEX `fk_match_stadium1_idx` (`stadium_id` ASC) VISIBLE,
  INDEX `fk_match_Domare1_idx` (`Domare_id` ASC) VISIBLE,
  INDEX `fk_match_lager1_idx` (`lager_namn` ASC) VISIBLE,
  CONSTRAINT `fk_match_stadium1`
    FOREIGN KEY (`stadium_id`)
    REFERENCES `VM`.`Stadium` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_match_Domare1`
    FOREIGN KEY (`Domare_id`)
    REFERENCES `VM`.`Domare` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_match_lager1`
    FOREIGN KEY (`lager_namn`)
    REFERENCES `VM`.`lager` (`namn`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION

) ENGINE = InnoDB;

-- -----------------------------------------------------
-- INSERT DATA INTO THE TABLES
-- -----------------------------------------------------

INSERT INTO `grupp`(namn)
VALUE ('A'), ('B'), ('C'), ('D'), ('E'), ('F'), ('G'), ('H');


INSERT INTO `lager` (namn, grupp_namn)
VALUE ('Nederländerna', 'A'), ('Senegal', 'A'), ('Ecuador', 'A'), ('Qatar', 'A'),
      ('England', 'B'), ('Wales', 'B'), ('USA', 'B'), ('Iran', 'B'),
      ('Argentina', 'C'), ('Polen', 'C'), ('Mexiko', 'C'), ('Saudiarabien', 'C'),
	  ('Frankrike', 'D'), ('Danmark', 'D'), ('Tunisien', 'D'), ('Australien', 'D'),   
      ('Spanien', 'E'), ('Tyskland', 'E'), ('Japan', 'E'), ('Costa Rica', 'E'),
      ('Belgien', 'F'), ('Kroatien', 'F'), ('Marocko', 'F'), ('Kanada', 'F'),
      ('Brasilien', 'G'), ('Schweiz', 'G'), ('Serbien', 'G'), ('Kamerun', 'G'), 
      ('Portugal', 'H'), ('Uruguay', 'H'), ('Sydkorea', 'H'), ('Ghana', 'H');
        

INSERT INTO `Domare` (id, namn, efternamn, land)
VALUE (1, `Abdulrahman`, `Al Jassim`, `Qatar`),
	  (2, `Ivan`, ` Barton`, `El Frälsning`),
	  (3, `Chris`, ` Beath`, `Australien`),
	  (4, `Raphael`, ` Claus`, `Brasilien`),
	  (5, `Matthew`, ` Conger`, `Nya Zeeland`),
	  (6, `Ismail`, ` Elfath`, `USA`),
	  (7, `Mario`, ` Escobar`, `Guatemala`),
	  (8, `Alireza`, ` Faghani`, `Iran`),
	  (9, `Stephanie`, ` Frappart`, `Frankrike`),
	  (10, `Bakary`, ` Gassama`, `Gambia`),
	  (11, `Mustafa`, ` Ghorbal`, `Algeriet`),
	  (12, `Victor`, ` Gomes`, `Sydafrika`),
	  (13, `Istvan`, ` Kovacs`, `Rumänien`),
	  (14, `Ning`, ` Ma`, `Kina`),
	  (15, `Danny`, ` McKelie`, `Nederländerna`),
	  (16, `Szymon`, ` Marciniak`, `Polen`),
	  (17, `Sade`, ` Martinez`, `Honduras`),
	  (18, `Antonio Matthew`, ` Lahoz`, `Spanien`),
	  (19, `Andres Matías`, ` Matonte Cabrera`, `Uruguay`),
	  (20, `Mohammed`, ` Abdullah Mohammed`, `Förenade Arabemiraten`),
	  (21, `Salima`, ` Mukansanga`, `Rwanda`),
	  (22, `Maguette`, ` Ndiaye`, `Senegal`),
	  (23, `Michael`, ` Oliver`, `England`),
	  (24, `Daniele`, ` Orsato`, `Italien`),
	  (25, `Kevin`, ` Ortega`, `Peru`),
	  (26, `Cesar`, ` Ramos`, `Mexiko`),
	  (27, `Fernando`, ` Rapallini`, `Argentina`),
	  (28, `Wilton`, ` Sampaio`, `Brasilien`),
	  (29, `Daniel`, ` Siebert`, `Tyskland`),
	  (30, `Janny`, ` Sikazwe`, `Zambia`),
	  (31, `Anthony`, ` Taylor`, `England`),
	  (32, `Facundo`, ` Tello`, `Argentina`),
	  (33, `Clement`, ` Turpin`, `Frankrike`),
	  (34, `Jesus`, ` Valenzuela`, `Venezuela`),
	  (35, `Slavko`, ` Vincic`, `Slovenien`),
	  (36, `Yoshimi`, ` Yamashita`, `Japan`);


INSERT INTO `VM`.`Stadium`(id, namn, stad, kapacitet)
VALUE (1, `Lusail Iconic Stadium`,	`Lusail`, 86250),
	  (2, `Al-Bayt Stadium`, `Al Khor`, 60000),
	  (3, `Al Janoub Stadium`,	`Al Wakrah`, 40000),
	  (4, `Education City Stadium`,	`Doha`, 45350),
	  (5, `Stadio Ras Abu Abdou`,	`Doha`, 44950),
	  (6, `Al Thumama Stadium`,	`Doha`, 40000),
	  (7, `Ahmed bin Ali Stadium`,	`Ar Rayyan`, 44000),
	  (8, `Khalifa International Stadium`,	`Doha`, 48000);


-- Till exempel Nederländerna mot Senegal
-- https://bettingstugan.se/match/infor-senegal-nederlanderna-vm-2022

INSERT INTO `match` (id, n_match, stadium_id, datum, Domare_id, lager_namn, poang, gjorda_mål, insläppta_mål)
VALUE 	(1, 1, 6, '2022-11-21', 28, 'Nederländerna', 3, 2, 0),
		(2, 1, 6, '2022-11-21', 28, 'Senegal', 0, 0, 2);


