-- phpMyAdmin SQL Dump
-- version 4.0.10deb1
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Apr 12, 2015 at 07:49 PM
-- Server version: 5.5.41-0ubuntu0.14.04.1
-- PHP Version: 5.5.23-1+deb.sury.org~trusty+2

-- @Author : Debapriya Das
-- 	3rd Year - UG, CSE DEPT, NIT DURGAPUR



SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+05s:30";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `geeksforgeeks`
--
CREATE DATABASE IF NOT EXISTS `geeksforgeeks` DEFAULT CHARACTER SET latin1 COLLATE latin1_swedish_ci;
USE `geeksforgeeks`;

-- --------------------------------------------------------

--
-- Table structure for table `Records`
--
-- Creation: Apr 12, 2015 at 12:59 PM
--

DROP TABLE IF EXISTS `Records`;
CREATE TABLE IF NOT EXISTS `Records` (
  `serial_no` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(30) NOT NULL,
  `search_string` varchar(30) NOT NULL,
  `email` varchar(40) DEFAULT NOT NULL,
  PRIMARY KEY (`serial_no`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

--
-- Dumping data for table `Records`
--


/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
