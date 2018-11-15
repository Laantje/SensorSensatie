-- phpMyAdmin SQL Dump
-- version 4.8.3
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Nov 15, 2018 at 12:56 PM
-- Server version: 5.7.23
-- PHP Version: 7.2.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `zengltd`
--

-- --------------------------------------------------------

--
-- Table structure for table `ramen`
--

DROP TABLE IF EXISTS `ramen`;
CREATE TABLE IF NOT EXISTS `ramen` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `naam` varchar(20) NOT NULL,
  `poort` int(2) NOT NULL,
  `type` varchar(1) NOT NULL,
  `status` varchar(1) NOT NULL,
  `mode` varchar(1) NOT NULL,
  `uitrolstand` int(3) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `ramen`
--

INSERT INTO `ramen` (`id`, `naam`, `poort`, `type`, `status`, `mode`, `uitrolstand`) VALUES
(2, 'raam1', 5, '1', '1', '1', 50);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
