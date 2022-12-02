-- MySQL Script generated by MySQL Workbench
-- mer 23 nov 2022, 10:26:29
-- Model: New Model    Version: 1.0
-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema jultomtens databas
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `jultomtens databas` ;

-- -----------------------------------------------------
-- Schema jultomtens databas
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `jultomtens databas` ;
USE `jultomtens databas` ;

-- -----------------------------------------------------
-- Table `jultomtens databas`.`Presenter`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `jultomtens databas`.`Presenter` ;

CREATE TABLE IF NOT EXISTS `jultomtens databas`.`Presenter` (
  `id` INT NOT NULL,
  `namn` VARCHAR(255) NOT NULL,
  `beskrivning` VARCHAR(255) NULL DEFAULT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `jultomtens databas`.`Önskelistor`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `jultomtens databas`.`Önskelistor` ;

CREATE TABLE IF NOT EXISTS `jultomtens databas`.`Önskelistor` (
  `id` INT NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `jultomtens databas`.`Länder`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `jultomtens databas`.`Länder` ;

CREATE TABLE IF NOT EXISTS `jultomtens databas`.`Länder` (
  `namn` VARCHAR(255) NOT NULL,
  PRIMARY KEY (`namn`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `jultomtens databas`.`Barn`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `jultomtens databas`.`Barn` ;

CREATE TABLE IF NOT EXISTS `jultomtens databas`.`Barn` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `namn` VARCHAR(255) NOT NULL,
  `gata` VARCHAR(255) NOT NULL,
  `nr` INT NOT NULL,
  `ord` VARCHAR(255) NOT NULL,
  `postord` INT NOT NULL,
  `Presenter_id` INT NOT NULL,
  `Önskelistor_id` INT NOT NULL,
  `Länder_namn` VARCHAR(255) NOT NULL,
  PRIMARY KEY (`id`, `Presenter_id`, `Önskelistor_id`, `Länder_namn`),
  CONSTRAINT `fk_Barn_Presenter1`
    FOREIGN KEY (`Presenter_id`)
    REFERENCES `jultomtens databas`.`Presenter` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Barn_Önskelistor1`
    FOREIGN KEY (`Önskelistor_id`)
    REFERENCES `jultomtens databas`.`Önskelistor` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Barn_Länder1`
    FOREIGN KEY (`Länder_namn`)
    REFERENCES `jultomtens databas`.`Länder` (`namn`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

CREATE INDEX `fk_Barn_Presenter1_idx` ON `jultomtens databas`.`Barn` (`Presenter_id` ASC) VISIBLE;

CREATE INDEX `fk_Barn_Önskelistor1_idx` ON `jultomtens databas`.`Barn` (`Önskelistor_id` ASC) VISIBLE;

CREATE INDEX `fk_Barn_Länder1_idx` ON `jultomtens databas`.`Barn` (`Länder_namn` ASC) VISIBLE;


-- -----------------------------------------------------
-- Table `jultomtens databas`.`Önskar`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `jultomtens databas`.`Önskar` ;

CREATE TABLE IF NOT EXISTS `jultomtens databas`.`Önskar` (
  `ordning plats` INT NOT NULL,
  `besrkivning` VARCHAR(255) NULL DEFAULT NULL,
  `namn` VARCHAR(255) NOT NULL,
  `Önskelistor_id` INT NOT NULL,
  PRIMARY KEY (`namn`, `Önskelistor_id`),
  CONSTRAINT `fk_Önskar_Önskelistor`
    FOREIGN KEY (`Önskelistor_id`)
    REFERENCES `jultomtens databas`.`Önskelistor` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

CREATE INDEX `fk_Önskar_Önskelistor_idx` ON `jultomtens databas`.`Önskar` (`Önskelistor_id` ASC) VISIBLE;


-- -----------------------------------------------------
-- Table `jultomtens databas`.`Presenter_has_Önskelistor`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `jultomtens databas`.`Presenter_has_Önskelistor` ;

CREATE TABLE IF NOT EXISTS `jultomtens databas`.`Presenter_has_Önskelistor` (
  `Presenter_id` INT NOT NULL,
  `Önskelistor_id` INT NOT NULL,
  PRIMARY KEY (`Presenter_id`, `Önskelistor_id`),
  CONSTRAINT `fk_Presenter_has_Önskelistor_Presenter1`
    FOREIGN KEY (`Presenter_id`)
    REFERENCES `jultomtens databas`.`Presenter` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Presenter_has_Önskelistor_Önskelistor1`
    FOREIGN KEY (`Önskelistor_id`)
    REFERENCES `jultomtens databas`.`Önskelistor` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

CREATE INDEX `fk_Presenter_has_Önskelistor_Önskelistor1_idx` ON `jultomtens databas`.`Presenter_has_Önskelistor` (`Önskelistor_id` ASC) VISIBLE;

CREATE INDEX `fk_Presenter_has_Önskelistor_Presenter1_idx` ON `jultomtens databas`.`Presenter_has_Önskelistor` (`Presenter_id` ASC) VISIBLE;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
