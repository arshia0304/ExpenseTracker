-- phpMyAdmin SQL Dump
-- version 4.9.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Aug 20, 2020 at 01:05 PM
-- Server version: 10.4.8-MariaDB
-- PHP Version: 7.3.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `expense_tracker`
--

-- --------------------------------------------------------

--
-- Table structure for table `expense_table`
--

CREATE TABLE `expense_table` (
  `name` varchar(30) NOT NULL,
  `amount` decimal(10,2) NOT NULL,
  `date` varchar(10) NOT NULL,
  `day` varchar(10) NOT NULL,
  `week_no` int(11) NOT NULL,
  `weekly_limit` decimal(10,2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `expense_table`
--

INSERT INTO `expense_table` (`name`, `amount`, `date`, `day`, `week_no`, `weekly_limit`) VALUES
('Internet Charges', '750.00', '08/01/20', 'Saturday', 1, '10000.00'),
('Mobile Bill', '349.00', '08/01/20', 'Saturday', 1, '10000.00'),
('Food', '620.00', '08/01/20', 'Saturday', 1, '10000.00'),
('Food', '350.00', '08/02/20', 'Sunday', 2, '9200.00'),
('Flowers', '99.00', '08/02/20', 'Sunday', 2, '9200.00'),
('Mattress', '850.00', '08/02/20', 'Sunday', 2, '9200.00'),
('Travelling', '60.00', '08/03/20', 'Monday', 2, '9200.00'),
('Parcel', '50.00', '08/03/20', 'Monday', 2, '9200.00'),
('Earphones', '499.00', '08/03/20', 'Monday', 2, '9200.00'),
('Pillow', '399.00', '08/04/20', 'Tuesday', 2, '9200.00'),
('Charger', '299.00', '08/04/20', 'Tuesday', 2, '9200.00'),
('Pens', '109.00', '08/04/20', 'Tuesday', 2, '9200.00'),
('Medicine', '678.00', '08/05/20', 'Wednesday', 2, '9200.00'),
('Bag', '799.00', '08/05/20', 'Wednesday', 2, '9200.00'),
('Food', '200.00', '08/05/20', 'Wednesday', 2, '9200.00'),
('Water Bill', '600.00', '08/06/20', 'Thursday', 2, '9200.00'),
('Flower', '250.00', '08/06/20', 'Thursday', 2, '9200.00'),
('Food', '350.00', '08/06/20', 'Thursday', 2, '9200.00'),
('Electricity Bill', '850.00', '08/07/20', 'Friday', 2, '9200.00'),
('Shopping', '605.00', '08/07/20', 'Friday', 2, '9200.00'),
('Router', '999.00', '08/08/20', 'Saturday', 2, '9200.00'),
('Google Cloud', '350.00', '08/08/20', 'Saturday', 2, '9200.00'),
('AWS', '650.00', '08/08/20', 'Saturday', 2, '9200.00'),
('Parcel', '70.00', '08/09/20', 'Sunday', 3, '12000.00'),
('Food', '580.00', '08/09/20', 'Sunday', 3, '12000.00'),
('Ice Cream', '150.00', '08/09/20', 'Sunday', 3, '12000.00'),
('Travelling', '250.00', '08/10/20', 'Monday', 3, '12000.00'),
('Medicine', '210.00', '08/10/20', 'Monday', 3, '12000.00'),
('Doctor', '200.00', '08/10/20', 'Monday', 3, '12000.00'),
('Beverages', '340.00', '08/11/20', 'Tuesday', 3, '12000.00'),
('Muffins', '150.00', '08/11/20', 'Tuesday', 3, '12000.00'),
('Chips', '600.00', '08/11/20', 'Tuesday', 3, '12000.00'),
('Sweets', '500.00', '08/12/20', 'Wednesday', 3, '12000.00'),
('Curd', '100.00', '08/12/20', 'Wednesday', 3, '12000.00'),
('Juices', '451.00', '08/12/20', 'Wednesday', 3, '12000.00'),
('Fruits', '650.00', '08/13/20', 'Thursday', 3, '12000.00'),
('Vegetable', '85.00', '08/14/20', 'Friday', 3, '12000.00'),
('Grocery', '850.00', '08/14/20', 'Friday', 3, '12000.00'),
('TV Repairing', '800.00', '08/14/20', 'Friday', 3, '12000.00'),
('Food', '350.00', '08/15/20', 'Saturday', 3, '12000.00'),
('Juice', '300.00', '08/15/20', 'Saturday', 3, '12000.00'),
('Butteer', '50.00', '08/15/20', 'Saturday', 3, '12000.00'),
('Cheese', '300.00', '08/15/20', 'Saturday', 3, '12000.00'),
('Flowers', '250.00', '08/16/20', 'Sunday', 4, '15000.00'),
('Perfume', '999.00', '08/16/20', 'Sunday', 4, '15000.00'),
('Hand Sanitizer', '149.00', '08/16/20', 'Sunday', 4, '15000.00'),
('Pet Food', '230.00', '08/17/20', 'Monday', 4, '15000.00'),
('Food', '148.00', '08/17/20', 'Monday', 4, '15000.00'),
('House Rent', '2000.00', '08/17/20', 'Monday', 4, '15000.00'),
('Wordpress', '359.00', '08/18/20', 'Tuesday', 4, '15000.00'),
('Hair Cut', '100.00', '08/18/20', 'Tuesday', 4, '15000.00'),
('Shaving', '50.00', '08/18/20', 'Tuesday', 4, '15000.00'),
('Travelling', '380.00', '08/19/20', 'Wednesday', 4, '15000.00'),
('Food', '256.00', '08/19/20', 'Wednesday', 4, '15000.00'),
('Battery', '500.00', '08/19/20', 'Wednesday', 4, '15000.00'),
('Breakfast', '60.00', '08/20/20', 'Thursday', 4, '15000.00'),
('Salad', '80.00', '08/20/20', 'Thursday', 4, '15000.00'),
('Laundry Bill', '439.00', '08/20/20', 'Thursday', 4, '15000.00');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
