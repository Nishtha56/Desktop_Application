-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 01, 2023 at 01:38 PM
-- Server version: 10.4.24-MariaDB
-- PHP Version: 7.4.29

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `hotel_manager_db`
--

-- --------------------------------------------------------

--
-- Table structure for table `booking_table`
--

CREATE TABLE `booking_table` (
  `Reg_No` int(10) NOT NULL,
  `Name` varchar(200) NOT NULL,
  `Phone` bigint(30) NOT NULL,
  `UID` bigint(30) NOT NULL,
  `Check_In` date NOT NULL,
  `Check_Out` date NOT NULL,
  `Total_guests` int(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `booking_table`
--

INSERT INTO `booking_table` (`Reg_No`, `Name`, `Phone`, `UID`, `Check_In`, `Check_Out`, `Total_guests`) VALUES
(1, 'aman', 1234567898, 1234567898, '2023-04-19', '2023-04-28', 3),
(2, 'naman', 9988991122, 99889911224, '2023-04-27', '2023-04-28', 2);

-- --------------------------------------------------------

--
-- Table structure for table `roominfo_table`
--

CREATE TABLE `roominfo_table` (
  `Reg_No` int(10) NOT NULL,
  `Room_Type` varchar(100) NOT NULL,
  `Room_no` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `roominfo_table`
--

INSERT INTO `roominfo_table` (`Reg_No`, `Room_Type`, `Room_no`) VALUES
(2, 'AC', '102'),
(1, 'Non AC', '103');

-- --------------------------------------------------------

--
-- Table structure for table `usertable`
--

CREATE TABLE `usertable` (
  `username` varchar(20) NOT NULL,
  `password` varchar(20) NOT NULL,
  `usertype` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `usertable`
--

INSERT INTO `usertable` (`username`, `password`, `usertype`) VALUES
('raman', '1234', 'Admin'),
('riya', '456', 'Employee');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `booking_table`
--
ALTER TABLE `booking_table`
  ADD PRIMARY KEY (`Reg_No`);

--
-- Indexes for table `roominfo_table`
--
ALTER TABLE `roominfo_table`
  ADD PRIMARY KEY (`Room_no`) USING BTREE;

--
-- Indexes for table `usertable`
--
ALTER TABLE `usertable`
  ADD PRIMARY KEY (`username`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
