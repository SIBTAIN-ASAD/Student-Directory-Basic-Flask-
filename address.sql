-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Dec 07, 2021 at 10:00 AM
-- Server version: 10.4.20-MariaDB
-- PHP Version: 7.3.29

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `address`
--

-- --------------------------------------------------------

--
-- Table structure for table `addressbook`
--

CREATE TABLE `addressbook` (
  `contact_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `Contact_name` varchar(50) DEFAULT NULL,
  `Contact_mobile` varchar(15) DEFAULT NULL,
  `Contact_city` varchar(50) DEFAULT NULL,
  `Contact_profession` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `addressbook`
--

INSERT INTO `addressbook` (`contact_id`, `user_id`, `Contact_name`, `Contact_mobile`, `Contact_city`, `Contact_profession`) VALUES
(3, 6, 'MAlIK G', '0356233453', 'Murree', 'DON'),
(4, 6, 'MAlIK G', '0356233453', 'Murree', 'DON'),
(28, 6, 'Sibtain Asad', '0345734', 'Lahore', 'coder');

-- --------------------------------------------------------

--
-- Table structure for table `admin`
--

CREATE TABLE `admin` (
  `admin_id` int(10) NOT NULL,
  `admin_name` varchar(20) NOT NULL,
  `admin_pwd` varchar(20) NOT NULL,
  `admin_email` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `admin`
--

INSERT INTO `admin` (`admin_id`, `admin_name`, `admin_pwd`, `admin_email`) VALUES
(1, 'RMS ADMIN', 'admin', 'admin@gmail.com'),
(2, 'Admin2', 'admin2', 'admin2@yahoo.com'),
(3, 'admin3', 'admin3', 'admin3@'),
(4, 'test', 'test', 'test');

-- --------------------------------------------------------

--
-- Table structure for table `dish`
--

CREATE TABLE `dish` (
  `d_id` int(10) NOT NULL,
  `d_name` varchar(30) NOT NULL,
  `d_ingredients` varchar(30) NOT NULL,
  `d_price` varchar(30) NOT NULL,
  `d_category` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `dish`
--

INSERT INTO `dish` (`d_id`, `d_name`, `d_ingredients`, `d_price`, `d_category`) VALUES
(1, 'Satay', '1', '30', 'Meat'),
(2, 'nougat', '2', '40', 'dessert'),
(3, 'Fish', '3', '100', 'seafood'),
(4, 'Pizza', '5', '30', 'FastFood');

-- --------------------------------------------------------

--
-- Table structure for table `ingredients`
--

CREATE TABLE `ingredients` (
  `i_id` int(10) NOT NULL,
  `first` varchar(30) NOT NULL,
  `second` varchar(30) NOT NULL,
  `third` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `ingredients`
--

INSERT INTO `ingredients` (`i_id`, `first`, `second`, `third`) VALUES
(1, 'meat', 'tofu', 'seafood'),
(2, 'torrone', 'mandolato', 'gaz'),
(3, 'cod', 'haddock', 'hake'),
(4, 'Cheez', 'Butter', 'Mayonees'),
(5, 'Cheez', 'Butter', 'Honey');

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `user_id` int(20) NOT NULL,
  `user_email` varchar(20) DEFAULT NULL,
  `user_password` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`user_id`, `user_email`, `user_password`) VALUES
(2, 'sibtain@gmail.com', '12345'),
(3, 'hassan@gmail.com', '4567'),
(4, '2345', '2345'),
(6, 'sam@gmail.com', '12345678'),
(10, 'sibtain@gmail.com', '3243465757345'),
(11, 'sibtain@gmail.com', '3243465757345'),
(13, 'sibtain@gmail.com', '235346633544');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `addressbook`
--
ALTER TABLE `addressbook`
  ADD PRIMARY KEY (`contact_id`),
  ADD KEY `FK_USERS` (`user_id`);

--
-- Indexes for table `admin`
--
ALTER TABLE `admin`
  ADD PRIMARY KEY (`admin_id`);

--
-- Indexes for table `dish`
--
ALTER TABLE `dish`
  ADD PRIMARY KEY (`d_id`);

--
-- Indexes for table `ingredients`
--
ALTER TABLE `ingredients`
  ADD PRIMARY KEY (`i_id`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`user_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `addressbook`
--
ALTER TABLE `addressbook`
  MODIFY `contact_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=29;

--
-- AUTO_INCREMENT for table `admin`
--
ALTER TABLE `admin`
  MODIFY `admin_id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `dish`
--
ALTER TABLE `dish`
  MODIFY `d_id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `ingredients`
--
ALTER TABLE `ingredients`
  MODIFY `i_id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `user`
--
ALTER TABLE `user`
  MODIFY `user_id` int(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `addressbook`
--
ALTER TABLE `addressbook`
  ADD CONSTRAINT `FK_USERS` FOREIGN KEY (`user_id`) REFERENCES `user` (`user_id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
